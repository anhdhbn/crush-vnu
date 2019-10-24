from jobqueue import tasks

def check_fresh_go(proxy):
    tasks.check_fresh_go.delay(proxy)