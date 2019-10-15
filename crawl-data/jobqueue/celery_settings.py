import os

CELERY_TASK_SERIALIZER = 'json'
BROKER_URL = os.getenv('REDIS_URL', 'redis://h:iQwNeRiLAt8wTxM68JhrMY1Hftz2W8EQ@SG-celery-26745.servers.mongodirector.com:6379') 
CELERY_ACCEPT_CONTENT = ['json']