import os
from celery.schedules import crontab
from jobqueue.utilities import create_schedule_proxies

CELERY_TASK_SERIALIZER = 'json'
BROKER_URL = os.getenv('REDIS_URL', 'redis://h:iQwNeRiLAt8wTxM68JhrMY1Hftz2W8EQ@SG-celery-26745.servers.mongodirector.com:6379') 
CELERY_ACCEPT_CONTENT = ['json']

CELERY_IMPORTS = ('jobqueue.proxies.tasks')

CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'Asia/Ho_Chi_Minh'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERYBEAT_SCHEDULE = create_schedule_proxies()
# CELERY_ENABLE_UTC=True
CELERY_TASK_PROTOCOL = 1

CELERY_TASK_DEFAULT_QUEUE = 'jobqueue.proxies.tasks'
CELERY_DEFAULT_QUEUE = 'jobqueue.proxies.tasks'
CELERY_ROUTES = {"jobqueue.proxies.tasks": {"queue": "jobqueue.proxies.tasks"}}