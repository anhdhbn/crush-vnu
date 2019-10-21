from crawler.proxies.proxies import GetProxies, Proxies
import re
from celery.schedules import crontab
from datetime import timedelta

class SocksProxyNet(GetProxies):
    time = crontab(minute="*/10")
    def get_proxies(self):
        site = "https://www.socks-proxy.net/"
        content = self.http.quickGetStr(site)
        elements = re.findall("(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3}).*?(\d{1,5}).*?Socks(\d{1})", content) 
        result = [ (f"{n1}.{n2}.{n3}.{n4}", n5, n6) for (n1, n2, n3, n4, n5, n6) in elements if n5.isdigit() and n6.isdigit()]
        result = [ Proxies(ip, port, version) for (ip, port, version) in result]
        return result