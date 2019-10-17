from crawler.init.initchilkat import InitChilkat

class CheckFresh(InitChilkat):
    def execute_script(self):
        return self.http.quickGetStr(f"http://ip-api.com/json/{self.ip}")