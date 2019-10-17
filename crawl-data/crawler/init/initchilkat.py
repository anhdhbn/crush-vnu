import chilkat
import sys
import os

class InitChilkat:
    def __init__(self, proxy=None):
        self.unlock_chilkat()
        self.init_http(proxy)

    def init_http(self, proxy=None):
        self.http = chilkat.CkHttp()
        self.http.put_CookieDir("memory")
        self.http.put_SaveCookies(True)
        self.http.put_SendCookies(True)
        if proxy is not None:
            self.http.put_SocksVersion(proxy['version'])
            self.http.put_SocksHostname(proxy['ip'])
            self.http.put_SocksPort(proxy['ip'])
            self.http.put_SocksUsername(proxy['username'])
            self.http.put_SocksPassword(proxy['password'])
            self.version = proxy['version']
            self.ip = proxy['ip']
            self.username = proxy['username']
            self.password = proxy['password']

    def unlock_chilkat(self):
        self.glob = chilkat.CkGlobal()
        success = self.glob.UnlockBundle(os.getenv("CHILKAT_KEY", "Anything for 30-day trial"))
        if (success != True):
            print(glob.lastErrorText())
            sys.exit()

        status = self.glob.get_UnlockStatus()
        if (status == 2):
            print("Unlocked using purchased unlock code.")
        else:
            print("Unlocked in trial mode.")