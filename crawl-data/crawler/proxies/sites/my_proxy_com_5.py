from crawler.proxies.proxies import GetProxies, Proxies
import re
from celery.schedules import crontab
from datetime import timedelta

class MyProxyCom5(GetProxies):
    time = crontab(minute="*")
    def execute_script(self):
        site = "https://www.my-proxy.com/free-socks-5-proxy.html"
        content = self.http.quickGetStr(site)
        elements = re.findall("(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3}).*?(\d{1,5})", content) 
        result = [ (f"{n1}.{n2}.{n3}.{n4}", n5) for (n1, n2, n3, n4, n5) in elements if n5.isdigit()]
        result = [ Proxies(ip, port, 5) for (ip, port) in result]
        self.add_proxies_to_queue(result)