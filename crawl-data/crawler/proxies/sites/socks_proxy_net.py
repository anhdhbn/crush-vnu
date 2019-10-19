from crawler.proxies.proxies import GetProxies
import re
from celery.schedules import crontab
from datetime import timedelta

class SocksProxyNet(GetProxies):
    time = crontab(minute="*")
    def execute_script(self):
        from jobqueue.producer.proxies import check_fresh
        site = "https://www.socks-proxy.net/"
        content = self.http.quickGetStr(site)
        elements = re.findall("(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3}).*?(\d{1,5}).*?Socks(\d{1})", content) 
        result = [ (f"{n1}.{n2}.{n3}.{n4}", n5, n6) for (n1, n2, n3, n4, n5, n6) in elements if n5.isdigit() and n6.isdigit()]
        result = [{
            'ip': ip,
            'port': int(port),
            'version': int(version),
            'username': '',
            'password': ''
        } for (ip, port, version) in result]
        [check_fresh(proxy) for proxy in result]

        
        