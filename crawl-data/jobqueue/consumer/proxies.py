def check_fresh(proxy):
    from crawler.proxies.check_fresh import CheckFresh
    checker = CheckFresh(proxy=proxy)
    print(checker.execute_script())
    