from crawler.proxies.proxies import GetProxies

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

def create_schedule():
    proxy_classes = inheritors(GetProxies)
    result = {}
    for class_ in proxy_classes:
        result[f'auto-scan-proxies-{class_.__name__}'] = {
            'task': 'jobqueue.tasks.scan_proxies',
            'schedule': class_.time,
            'args' : (class_,)
        }
    return result