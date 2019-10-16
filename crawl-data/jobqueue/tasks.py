from celery import Celery
from jobqueue.consumer import facebook

app = Celery()
app.config_from_object("jobqueue.celery_settings")

@app.task(name='jobqueue.tasks.download_image_from_fb')
def download_image_from_fb(image_obj):
    facebook.download_image_from_fb(image_obj)


@app.task(name='jobqueue.tasks.scan_socks_by_day')
def scan_socks_by_day():
    pass

@app.task(name='jobqueue.tasks.scan_socks_by_hour')
def scan_socks_by_hour():
    pass