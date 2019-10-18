from celery import Celery
from jobqueue.utilities import inheritors

app = Celery()
app.config_from_object("jobqueue.celery_settings")

@app.task(name='jobqueue.tasks.download_image_from_fb')
def download_image_from_fb(image_obj):
    from jobqueue.consumer import facebook
    facebook.download_image_from_fb(image_obj)


@app.task(name='jobqueue.tasks.scan_proxies')
def scan_proxies(class_site):
    temp = class_site()
    temp.execute_script()

@app.task(name='jobqueue.tasks.check_fresh')
def check_fresh(proxy):
    from jobqueue.consumer import proxies
    return proxies.check_fresh(proxy)