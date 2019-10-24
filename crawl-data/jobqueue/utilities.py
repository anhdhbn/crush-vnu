from crawler.proxies.proxies import GetProxies
from crawler.proxies.sites import *

def inheritors(klass):
    subclasses = set()
    work = [klass]
    while work:
        parent = work.pop()
        for child in parent.__subclasses__():
            if child not in subclasses:
                subclasses.add(child)
                work.append(child)
    return subclasses

def create_schedule_proxies():
    proxy_classes = inheritors(GetProxies)
    result = {}
    for class_ in proxy_classes:
        result[f'auto-scan-proxies-{class_.__name__}'] = {
            'task': 'jobqueue.tasks.scan_proxies',
            'schedule': class_.time,
            'args' : (class_.__name__,)
        }
    return result

def find_class_by_name(name):
    proxy_classes = inheritors(GetProxies)
    for proxy_class in proxy_classes:
        if proxy_class.__name__ == name:
            return proxy_class
    return None