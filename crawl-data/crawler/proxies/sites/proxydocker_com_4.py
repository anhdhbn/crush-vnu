from crawler.proxies.proxies import GetProxies, Proxies
import re
from celery.schedules import crontab
from datetime import timedelta
import chilkat
import json
from datetime import datetime

class ProxyDocker4(GetProxies):
    time = crontab(day_of_week="*")
    def get_proxies(self):
        # site = "https://www.proxydocker.com/en/api/proxylist/"
        i = 0
        self.stop = False
        result = []
        while(self.stop == False):
            req = self.make_req(i)
            resp = self.http.SynchronousRequest("www.proxydocker.com",443,True,req)
            temp = self.get_result(resp.bodyStr())
            i = i + 1
            result = result + temp
        return result

    def make_req(self, page):
        req = chilkat.CkHttpRequest()
        req.put_HttpVerb("POST")
        req.AddParam("type","socks4")
        req.AddParam("page", str(page))
        req.put_Path("/en/api/proxylist/")
        req.put_ContentType("multipart/form-data")
        req.AddHeader("Connection","Keep-Alive")
        return req
    
    def get_result(self, body):
        result = json.loads(body)
        now = datetime.strptime(result['now']['date'], '%Y-%m-%d %H:%M:%S.%f')
        proxies = result['proxies']
        
        if len(proxies) == 0:
            self.stop = True
        else:
            temp = now - datetime.strptime(proxies[-1]['lastcheck']['date'], '%Y-%m-%d %H:%M:%S.%f')
            if temp.total_seconds() > 3600*24:
                self.stop = True
        proxies = [Proxies(proxy['ip'], proxy['port'], proxy['type']) for proxy in proxies]       
        return proxies