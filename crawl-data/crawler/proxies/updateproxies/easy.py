from crawler.proxies.updateproxies.updateproxies import UpdateProxies
import re

class EasyUpdate(UpdateProxies):
    def execute_script(self):
        from jobqueue.producer.proxies import check_fresh
        sites = [
            "https://www.my-proxy.com/free-socks-5-proxy.html",
            "https://www.socks-proxy.net/"
        ]
        for site in sites:
            content = self.http.quickGetStr(site)
            elements = re.findall("(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3}).*?(\d{1,5})", content) 
            result = [ (f"{n1}.{n2}.{n3}.{n4}", n5) for (n1, n2, n3, n4, n5) in elements if n5.isdigit()]
            result = [{
                'ip': ip,
                'port': int(port),
                'version': 5,
                'username': '',
                'password': ''
            } for (ip, port) in result]
            [check_fresh(proxy) for proxy in result]

        
        