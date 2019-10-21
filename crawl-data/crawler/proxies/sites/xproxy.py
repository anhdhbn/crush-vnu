from crawler.proxies.proxies import GetProxies, Proxies
import re
from celery.schedules import crontab

class Xproxy(GetProxies):
    time = crontab(minute="*/10")
    def get_proxies(self):
        site = "https://www.xroxy.com/free-proxy-lists/?port=&type=All_socks&ssl=&country=&latency=&reliability="
        content = self.http.quickGetStr(site)
        pattern = "(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3}).*?(\d{1,5}).*?Socks(\d{1})"
        regex = re.compile(pattern, flags=re.MULTILINE|re.DOTALL)
        results = []
        for match in regex.finditer(content):
            results = results + [match.groups()]
        results = [ (f"{n1}.{n2}.{n3}.{n4}", n5, n6) for (n1, n2, n3, n4, n5, n6) in results if n5.isdigit() and n6.isdigit()]       
        results = [ Proxies(ip, port, version) for (ip, port, version) in results]
        return results