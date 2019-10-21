import chilkat
import sys
import os
import time
import js2py

class InitChilkat:
    def __init__(self, proxy=None):
        self.unlock_chilkat()
        self.init_http(proxy)
        self.timeout = 10
        self.resp = chilkat.CkHttpResponse()

    def init_http(self, proxy=None):
        self.http = chilkat.CkHttp()
        self.http.put_CookieDir("memory")
        self.http.put_SaveCookies(True)
        self.http.put_SendCookies(True)
        if proxy is not None:
            self.version = proxy['version']
            self.ip = proxy['ip']
            self.port = proxy['port']
            self.username = proxy['username']
            self.password = proxy['password']
            if self.version == 4 or self.version == 5:
                self.http.put_SocksVersion(self.version)
                self.http.put_SocksHostname(self.ip)
                self.http.put_SocksPort(self.port)
                self.http.put_SocksUsername(self.username)
                self.http.put_SocksPassword(self.password)
            else:
                self.http.put_ProxyDomain(self.ip)
                self.http.put_ProxyPort(self.port)
                self.http.put_ProxyLogin(self.username)
                self.http.put_ProxyPassword(self.password)
            
    def load_response(self, task):
        success = self.resp.LoadTaskResult(task)   
        return self.resp.bodyStr()

    def unlock_chilkat(self):
        self.glob = chilkat.CkGlobal()
        success = self.glob.UnlockBundle(os.getenv("CHILKAT_KEY", "Anything for 30-day trial"))
        if (success != True):
            print(glob.lastErrorText())
            sys.exit()