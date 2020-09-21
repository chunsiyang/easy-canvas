import datetime
import time

from app.core.service.canvas_service import get_course, get_modules, get_url, post_url
from app.core.service.modules_alert_history_service import get_history_by_course_id
from app.core.service.modules_alert_service import init_modules_history, scheduler_check_modules_update
from app.core.service.user_service import get_user, get_user_by_name

# print(get_course(get_user('admin', 'admin')))
#
#
# print(get_modules(get_user('admin', 'admin'), '27186'))
#
# init_modules_history()
scheduler_check_modules_update()

