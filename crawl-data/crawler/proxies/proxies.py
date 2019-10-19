from crawler.init.initchilkat import InitChilkat
class GetProxies(InitChilkat):
    def remove_duplicates(self, arr):
        return list(set(arr))
    def add_proxies_to_queue(self, arr):
        result = self.remove_duplicates(arr)
        from jobqueue.producer.proxies import check_fresh
        [check_fresh(proxy.conver_to_object()) for proxy in result]

class Proxies:
    def __init__(self, ip, port, version, username="", password=""):
        self.ip = ip
        self.port = port
        self.version = version
        self.username = username
        self.password = password
        self.hash = f"{self.ip}:{self.port}"

    def conver_to_object(self):
        return {
            'ip': self.ip,
            'port': int(self.port),
            'version': self.version,
            'username': self.username,
            'password': self.password
        }
    def __eq__(self, other):
        return self.hash == other.hash
    def __hash__(self):
        return hash(self.hash)
    def __repr__(self):
        return str(self.hash)