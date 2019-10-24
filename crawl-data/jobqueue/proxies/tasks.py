from celery import Celery
from jobqueue.utilities import inheritors

app = Celery("proxies")
app.config_from_object("jobqueue.proxies.celery_settings")

@app.task(name='jobqueue.proxies.tasks.scan_proxies')
def scan_proxies(class_name):
    from jobqueue.utilities import find_class_by_name
    class_ = find_class_by_name(class_name)
    if class_ is not None:
        get_proxy = class_()
        get_proxy.execute_script()

def check_fresh_go(proxy):
    app.send_task("jobqueue.proxies.tasks.check_fresh_go", (proxy,))