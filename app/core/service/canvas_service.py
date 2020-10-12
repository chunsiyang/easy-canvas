import copy

import requests


def get_url(user, url):
    """
        send http get request to canvas rest api server
    : param user user contain canvas address and canvas access token
    : param url rest api path
    :return: python requests respond
    """
    headers = {
        'Authorization': 'Bearer %s' % user.get('accessToken')
    }
    respond = requests.get(url, headers=headers)
    return respond


def post_url(user, url):
    """
        send http get request to canvas rest api server
    : param user user contain canvas address and canvas access token
    : param url rest api path
    :return: python requests respond
    """
    headers = {
        'Authorization': 'Bearer %s' % user.get('accessToken')
    }
    respond = requests.post(url, headers=headers)
    return respond


def get_user(user):
    """
    : param user
    :return: python requests respond
    """
    headers = {
        'Authorization': 'Bearer %s' % user.get('accessToken')
    }
    respond = requests.get('%s/api/v1/users/self' % user.get('canvasAddress'), headers=headers)
    return respond


def get_course(user):
    """
        get course info
    : param user user contain canvas address and canvas access token
    :return: json
    """
    respond = get_url(user, '%s/api/v1/courses?per_page=100' % user.get('canvasAddress'))
    return respond.json()


def get_modules(user, course):
    """
        get modules info
    : param user user contain canvas address and canvas access token
    : param course course id
    :return: json all course modules with sub items and pages (canvas restapi respond json)
    """
    json = get_url(user, '%s/api/v1/courses/%s/modules?per_page=100' % (user.get('canvasAddress'), course)).json()
    modules = copy.deepcopy(json)
    if modules:
        for module in modules:
            items_url = module.get('items_url')
            if items_url:
                module.update({'items': get_url(user, items_url+'?per_page=100').json()})
            items = module.get('items')
            if items:
                for item in items:
                    if item.get('type') == 'File':
                        file = get_url(user, item.get('url')+'?per_page=100').json()
                        item.update({'File': file})
                    if item.get('type') == 'Page':
                        page = get_url(user, item.get('url')+'?per_page=100').json()
                        item.update({'Page': page})
    return modules


def send_canvas_email(user, receive, message):
    """
        use canvas sent email
    : param user user contain canvas address and canvas access token
    : param receive receive user id
    : param message message to send
    """

    post_url(user, '%s/api/v1/conversations?recipients[]=%s&body=%s' % (user.get('canvasAddress'), receive, message))
