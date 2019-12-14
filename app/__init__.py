import logging
from flask import Flask
from flask_rq2 import RQ
import rq_dashboard

APP = Flask(__name__)
APP.config.from_pyfile('config.py')

#APP.config.from_object(rq_dashboard.default_settings)
APP.register_blueprint(rq_dashboard.blueprint, url_prefix='/rq')
RQ_CLIENT = RQ(APP)

from app import routes, cmds
# logging.info('initialized app')
