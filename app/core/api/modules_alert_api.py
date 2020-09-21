from flask import Blueprint, request

from app.core.aop.authority import authentication
from app.core.model.request_model import RequestModel
from app.core.model.respond_model import RespondModel
from app.core.service.modules_alert_service import get_setting_by_username, save_user_setting
from app.tools.jwt_tools import decode_jwt

api = Blueprint('modules_alert_api', __name__)


@api.route('/modulesalert/setting', methods=['get'])
@authentication
def get_setting():
    """
        get setting
    :return: respond model
    """
    request_model = RequestModel(request)
    respond_model = RespondModel()
    jwt = request_model.token
    user_info_jwt = decode_jwt(jwt)['user_info']
    setting = get_setting_by_username(user_info_jwt.get('name'))
    if setting:
        respond_model.data = setting.get('setting')
    else:
        respond_model.data = {}
    return respond_model


@api.route('/modulesalert/setting', methods=['post'])
@authentication
def save_setting():
    """
        save setting
    :return: respond model
    """
    request_model = RequestModel(request)
    respond_model = RespondModel()
    jwt = request_model.token
    user_info_jwt = decode_jwt(jwt)['user_info']
    save_user_setting(user_info_jwt.get('name'), request_model.data)
    return respond_model
