from celery import Celery
from jobqueue.consumer import facebook

app = Celery()
app.config_from_object("jobqueue.celery_settings")

@app.task(name='tasks.download_image_from_fb')
def download_image_from_fb(image_obj):
    facebook.download_image_from_fb(image_obj)