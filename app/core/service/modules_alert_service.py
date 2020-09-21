import datetime
import time

from app.core.service.canvas_service import get_course, get_modules, sent_email, get_user
from app.core.service.modules_alert_history_service import get_history_by_course_id, save_modules_histories, \
    clear_history
from app.core.service.user_service import get_user_by_name
from app.tools.db_tools import get_collection


def get_setting_by_username(username):
    """
        get user modules alert setting by username
    : param username
    :return: settings in list
    """
    collection = get_collection("modules_alert")
    setting = collection.find_one({'user': username})
    return setting


def save_user_setting(username, data):
    """
        save (insert or update) user modules alert setting
    : param username
    : param data  user modules alert setting
    :return:
    """
    collection = get_collection("modules_alert")
    setting = collection.find_one({'user': username})
    data = {'user': username, 'setting': data}
    if setting:
        collection.update({'user': username}, data)
    else:
        collection.insert(data)


def get_all_modules_setting():
    """
        get all modules settings
    :return: settings in mongo list
    """
    collection = get_collection('modules_alert')
    settings = collection.find()
    return settings


def get_all_modules_setting_enable():
    """
        get modules settings which is enabled
    :return: settings in mongo list
    """
    collection = get_collection('modules_alert')
    settings = collection.find({'setting.enable': True})
    return settings


def get_user_modules_from_canvas(user_name):
    """
        get modules information from canvas by user name
    :return:
        dict {
            'course' : course info (canvas restapi respond json),
            'modules' : all course modules with sub items and pages (canvas restapi respond json)
        }
    """
    histories = []
    user = get_user_by_name(user_name)
    courses = get_course(user)
    for course in courses:
        course_id = course.get('id')
        modules = get_modules(user, course_id)
        history = {
            'course': course,
            'modules': modules
        }
        histories.append(history)
    return histories


def get_modules_from_canvas():
    """
        get modules information from canvas
    :return:
        dict {
            'course' : course info (canvas restapi respond json),
            'modules' : all course modules with sub items and pages (canvas restapi respond json)
        }
    """
    settings = get_all_modules_setting()
    histories = []
    for setting in settings:
        user_name = setting.get('user')
        user = get_user_by_name(user_name)
        courses = get_course(user)
        for course in courses:
            course_id = course.get('id')
            modules = get_modules(user, course_id)
            if get_history_by_course_id(course_id):
                continue
            history = {
                'course': course,
                'modules': modules
            }
            histories.append(history)
    return histories


def transform_modules_json_to_dict(json):
    """
        transform canvas respond json to dict
    : param json canvas respond json
    :return:
        dict {
            course_id: {
                name: course name,
                modules_id: {
                    name: modules name,
                    item_id: {
                        name: item name,
                        type: item type,
                        update_at: update time,
                    }
                }
            }
        }
    """
    modules_dict = {}
    if not json:
        return {}
    for json_item in json:
        modules = json_item.get('modules')
        course_id = json_item.get('course').get('id')
        course_modules = {
            'name': json_item.get('course').get('name'),
            'course_id': str(course_id),
            }
        modules_dict.update({str(course_id): course_modules})
        for module in modules:
            modules_item = {'name': module.get('name')}
            course_modules.update({str(module.get('id')): modules_item})
            items = module.get('items')
            if items:
                for item in items:
                    item_dict = {}
                    modules_item.update({str(item.get('id')): item_dict})
                    item_type = item.get('type')
                    item_dict.update({'type': item_type})
                    item_dict.update({'name': item.get('title')})
                    if item_type == 'Page':
                        update_at = item.get('Page').get('updated_at')
                        item_dict.update({'update_at': update_at})
                    if item_type == 'File':
                        update_at = item.get('File').get('updated_at')
                        item_dict.update({'update_at': update_at})
    return modules_dict


def init_modules_history():
    """
        init modules history
        clean modules alert history database
        get and save new modules info
    :return:
    """
    clear_history()
    modules_json = get_modules_from_canvas()
    modules_dict = transform_modules_json_to_dict(modules_json)
    save_modules_histories(list(modules_dict.values()))


def scheduler_check_modules_update():
    """
        scheduler task to check modules update and send message to user
    :return:
    """
    user_setting = get_all_modules_setting()
    course_modules_cache = {}
    for modules_setting in user_setting:
        new_things = {}
        setting = modules_setting.get('setting')
        if setting.get('enable'):
            course_json = get_user_modules_from_canvas(modules_setting.get('user'))
            course_dict = transform_modules_json_to_dict(course_json)
            course_keys = list(course_dict.keys())
            for course_id in course_keys:
                if course_modules_cache.get(course_id):
                    course_history = course_modules_cache.get(course_id)
                else:
                    course_history = get_history_by_course_id(course_id)
                course_modules_cache.update({course_id: course_dict.get(course_id)})
                if not course_history:
                    continue
                # check course modules
                course_canvas = course_dict.get(course_id)
                modules_canvas_key = course_canvas.keys()
                for modules_canvas_id in modules_canvas_key:
                    course_history.update({})
                    if not modules_canvas_id == 'course_id' and not modules_canvas_id == 'name':
                        # check if modules is new
                        modules_history = course_history.get(modules_canvas_id)
                        modules_canvas = course_canvas.get(modules_canvas_id)
                        item_keys = modules_canvas.keys()
                        for item_id in item_keys:
                            item_canvas = modules_canvas.get(item_id)
                            if not item_id == 'name':
                                if modules_history:
                                    item_history = modules_history.get(item_id)
                                    if item_canvas.get('type') == 'File' or item_canvas.get('type') == 'Page':
                                        if item_history:
                                            # check if item is updated
                                            canvas_update_time = datetime.datetime.strptime(item_history.get('update_at'),
                                                                                            "%Y-%m-%dT%H:%M:%SZ")
                                            history_update_time = datetime.datetime.strptime(item_canvas.get('update_at'),
                                                                                             "%Y-%m-%dT%H:%M:%SZ")
                                            if canvas_update_time > history_update_time:
                                                update_new_item_into_dict(course_canvas, modules_canvas,
                                                                          item_canvas, new_things)
                                        else:
                                            update_new_item_into_dict(course_canvas, modules_canvas, item_canvas,
                                                                      new_things)
                                else:
                                    update_new_item_into_dict(course_canvas, modules_canvas, item_canvas, new_things)
            if not new_things == {}:
                notify_user_update(modules_setting.get('user'), new_things)
    clear_history()
    save_modules_histories(list(course_modules_cache.values()))


def update_new_item_into_dict(course, modules, item, target_dict):
    """
        insert result to new_things[]
    : param course
    : param modules
    : param item
    : param target_dict
    :return:
    """
    if not target_dict.get(course.get('name')):
        target_dict.update({course.get('name'): {}})
    if not target_dict.get(course.get('name')).get(modules.get('name')):
        target_dict.get(course.get('name')).update({modules.get('name'): {}})
    target_dict.get(course.get('name')).get(modules.get('name')).update({item.get('name'): item})


def notify_user_update(user_name, new_things):
    """
        sent user what has updated
    : param user_name
    : param new_things
    :return:
    """
    user = get_user_by_name(user_name)
    modules_alert_setting = get_setting_by_username(user_name)
    if modules_alert_setting.get('setting').get('notificationMethod') == 'canvas':
        message = ''
        for course_name in new_things.keys():
            message += course_name + '\n'
            for modules_name in new_things.get(course_name).keys():
                message += '----' + modules_name + '\n'
                for item_name in new_things.get(course_name).get(modules_name).keys():
                    message += '--------' + new_things.get(course_name).get(modules_name).get(item_name).get('name') + '\n'
            message += '\n'
        canvas_user = get_user(user)
        message = message.replace('&', ' and ')
        sent_email(user, canvas_user.json().get('id'), message)
