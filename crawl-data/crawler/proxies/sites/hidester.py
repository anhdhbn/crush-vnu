from crawler.proxies.proxies import GetProxies, Proxies
import re
from celery.schedules import crontab
import json

class Hidester(GetProxies):
    time = crontab(hour="*/2")
    def get_proxies(self):
        self.http.put_Referer("https://hidester.com/proxylist/")
        body = self.http.quickGetStr("https://hidester.com/proxydata/php/data.php?mykey=data&offset=0&limit=100000&orderBy=latest_check&sortOrder=DESC")
        proxies = json.loads(body)
        result = [ Proxies(proxy['IP'], proxy['PORT'], 
            5 if proxy['type'] == 'socks5' else (4 if proxy['type'] == 'socks4' else 'http') ) for proxy in proxies]
        return result