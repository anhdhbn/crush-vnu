from crawler.init.initchilkat import InitChilkat
import chilkat

class CheckFresh(InitChilkat):
    def execute_script(self):
        # return self.http.quickGetStr(f"http://ip-api.com/json/")
        task = self.http.QuickGetObjAsync(f"http://ip-api.com/json/")
        task.Run()
        status = task.Wait(self.timeout * 1000)
        wasCanceled = task.Cancel()
        if(wasCanceled):
            return "Timeout"
        else:
            result = self.load_response(task)
            return result
