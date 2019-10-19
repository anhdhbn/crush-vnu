from celery import Celery
from jobqueue.utilities import inheritors

app = Celery()
app.config_from_object("jobqueue.celery_settings")

@app.task(name='jobqueue.tasks.download_image_from_fb')
def download_image_from_fb(image_obj):
    from jobqueue.consumer import facebook
    facebook.download_image_from_fb(image_obj)


@app.task(name='jobqueue.tasks.scan_proxies')
def scan_proxies(class_name):
    from jobqueue.utilities import find_class_by_name
    class_ = find_class_by_name(class_name)
    if class_ is not None:
        get_proxy = class_()
        get_proxy.execute_script()

@app.task(name='jobqueue.tasks.check_fresh')
def check_fresh(proxy):
    from jobqueue.consumer import proxies
    return proxies.check_fresh(proxy)