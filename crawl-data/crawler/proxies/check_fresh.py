from crawler.init.initchilkat import InitChilkat

class CheckFresh(InitChilkat):
    def execute_script(self):
        # return self.http.quickGetStr(f"http://ip-api.com/json/{self.ip}")
        task = self.http.QuickGetObjAsync(f"http://ip-api.com/json/")
        task.Run()
        status = task.Wait(self.timeout * 1000)
        if(status):
            result = self.load_response(task)
            return result
        else:
            task.Cancel()
