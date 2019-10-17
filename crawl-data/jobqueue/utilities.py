from crawler.proxies.dailyproxies.dailyproxies import DailyProxies
from crawler.proxies.updateproxies.updateproxies import UpdateProxies
from celery.schedules import crontab
from datetime import timedelta

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
            'schedule': crontab(day_of_week="*"),
            'args' : (class_,)
        }

    for class_ in update_classes:
        result[f'auto-scan-proxies-by-hour-{class_.__class__.__name__}'] = {
            'task': 'jobqueue.tasks.scan_proxies_by_hour',
            'schedule': crontab(hou="*/2"),
            'args' : (class_,)
        }
    result['test'] = {
        'task': 'jobqueue.tasks.test',
        'schedule': timedelta(seconds=1)
    }
    return result