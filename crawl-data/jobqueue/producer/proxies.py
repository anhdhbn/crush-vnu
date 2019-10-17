from jobqueue import tasks

def check_fresh(proxy):
    tasks.check_fresh.delay(proxy)