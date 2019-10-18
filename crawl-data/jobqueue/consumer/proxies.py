def check_fresh(proxy):
    from crawler.proxies.check_fresh import CheckFresh
    checker = CheckFresh(proxy=proxy)
    if checker.execute_script() is not None:
        print(checker.execute_script())
    