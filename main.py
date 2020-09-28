#! /usr/bin/env python
# -*- coding: utf-8 -*-
# ***********************************
import logging

# init project install packages
from app.tools.init_tools import init_app
init_app()

from app.core.service.modules_alert_service import scheduler_check_modules_update, init_modules_history
from app.tools.config_tools import APP_CONFIG, get_config
from app.tools.router_tools import register_blueprints

from flask import Flask
from flask_cors import *
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__, static_folder='front-end/dist/', static_url_path='')
app_config = get_config(APP_CONFIG)
CORS(app, supports_credentials=True)

# register blueprints
register_blueprints(app, 'app.core.api', 'api')

# init modules history
init_modules_history()

# scheduler task
scheduler = BackgroundScheduler()
scheduler.add_job(scheduler_check_modules_update, 'interval', seconds=1800)
scheduler.start()

# region start
if __name__ == "__main__":
    app.debug = app_config['DEBUG']
    app.run(
        host=app_config['HOST'],
        port=app_config['PORT'],
        use_reloader=False
    )

logging.basicConfig(level=logging.INFO)
