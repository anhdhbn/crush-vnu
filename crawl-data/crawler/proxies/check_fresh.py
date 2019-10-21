from crawler.init.initchilkat import InitChilkat
import time
import chilkat

class CheckFresh(InitChilkat):
    def execute_script(self):
        start = time.time()
        task = self.http.QuickGetObjAsync(f"http://ip-api.com/json/{self.ip}")
        task.Run()
        task.Wait(self.timeout * 1000)
        if(task.get_StatusInt() == 7):
            result = self.load_response(task)
            return result
