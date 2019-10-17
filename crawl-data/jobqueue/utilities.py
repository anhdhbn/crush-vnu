from crawler.proxies.dailyproxies.dailyproxies import DailyProxies
from crawler.proxies.updateproxies.updateproxies import UpdateProxies

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
    daily_classes = inheritors(DailyProxies)
    update_classes = inheritors(UpdateProxies)
    result = {}
    for class_ in daily_classes:
        result[f'auto-scan-proxies-by-day-{class_.__class__.__name__}'] = {
            'task': 'jobqueue.tasks.scan_proxies_by_day',
            'schedule': class_.time,
            'args' : (class_,)
        }

    for class_ in update_classes:
        result[f'auto-scan-proxies-by-hour-{class_.__class__.__name__}'] = {
            'task': 'jobqueue.tasks.scan_proxies_by_hour',
            'schedule': class_.time,
            'args' : (class_,)
        }
    return result