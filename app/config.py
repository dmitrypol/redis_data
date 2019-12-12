''' base config '''
import os
from logging.config import dictConfig
import redis

HOME_DIR = os.environ.get('home_dir')
LOGS_DIR = f'{HOME_DIR}logs/'
APP_ENV = os.environ.get("APP_ENV")
SECRET_KEY = 'foobar'

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_DB = 0

RQ_DASHBOARD_REDIS_URL = f'redis://{REDIS_HOST}:6379/1'
RQ_REDIS_URL = f'redis://{REDIS_HOST}:6379/1'
RQ_QUEUES = ['high', 'default', 'low']

MAX_GITHUB_REQUESTS = 10
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '{timestamp:%(asctime)s, level:%(levelname)s, module:%(module)s, %(message)s}',
    }},
    'handlers': {
            'file': {
                'level': 'INFO',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'formatter': 'default',
                'filename': f'{LOGS_DIR}redis-data-{APP_ENV}.log',
                'when': 'D',
                'interval': 1,
                'backupCount': 7
            }
        },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})
