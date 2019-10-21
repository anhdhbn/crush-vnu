from crawler.init.initchilkat import InitChilkat

class CheckFresh(InitChilkat):
    def execute_script(self):
        # return self.http.quickGetStr(f"http://ip-api.com/json/{self.ip}")
        task = self.http.QuickGetStrAsync(f"http://ip-api.com/json/")
        task.Run()
        status = task.Wait(self.timeout * 1000)
        wasCanceled = task.Cancel()
        if(wasCanceled):
            return "Timeout"
        else:
            result = task.getResultString()
            return result
