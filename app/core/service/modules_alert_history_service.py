from app.tools.db_tools import get_collection


def save_modules_history(history):
    collection = get_collection('modules_alert_history')
    collection.insert(history)


def save_modules_histories(histories):
    for history in histories:
        save_modules_history(history)


def get_history_by_course_id(course_id):
    collection = get_collection('modules_alert_history')
    history = collection.find_one({'course_id': course_id})
    return history


def clear_history():
    collection = get_collection('modules_alert_history')
    collection.drop()
