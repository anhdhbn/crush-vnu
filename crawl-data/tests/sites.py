from crawler.proxies.sites import *
import unittest
import pytest

class SiteProxies(unittest.TestCase):
    def test(self):
        tester = proxy_list.ProxyListDownload4()
        assert len(tester.get_proxies()) > 3000

    def test2(self):
        tester = proxy_list.ProxyListDownload5()
        assert len(tester.get_proxies()) > 50

    def test3(self):
        tester = my_proxy.MyProxyCom4()
        assert len(tester.get_proxies()) > 50

    def test4(self):
        tester = my_proxy.MyProxyCom5()
        assert len(tester.get_proxies()) > 50

    def test5(self):
        tester = socks_proxy.SocksProxyNet()
        assert len(tester.get_proxies()) > 50

    def test6(self):
        tester = proxydocker.ProxyDocker4()
        assert len(tester.get_proxies()) == 20

    def test7(self):
        tester = proxydocker.ProxyDocker5()
        assert len(tester.get_proxies()) == 20

    def test8(self):
        tester = hidester.Hidester()
        assert len(tester.get_proxies()) > 1000