from crawler.init.initchilkat import InitChilkat
class DailyProxies(InitChilkat):
    def execute_script(self):
        print("Hello", self.__class__.__name__)