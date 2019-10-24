package main

import (
	"fmt"
	"io/ioutil"
	"net/http"

	"golang.org/x/net/proxy"
	"h12.io/socks"
)

const (
	// URL :This is url to check fresh
	// TIMEOUT :This is timeout

	URL         = "http://ip-api.com/json/"
	TIMEOUT int = 10
)

func checkFresh(proxyinfo map[string]interface{}) string {
	proxyURI := proxyinfo["proxyURI"].(string)
	fmt.Println(proxyURI)
	dialSocksProxy := socks.Dial(proxyURI)
	tr := &http.Transport{Dial: dialSocksProxy}
	httpClient := &http.Client{Transport: tr}
	resp, err := httpClient.Get(URL)
	if err != nil {
		return "Error"
	}
	defer resp.Body.Close()
	buf, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return "Error"
	}
	result := string(buf)
	fmt.Println(result)
	return result
}

func checkFresh2(proxyinfo map[string]interface{}) string {
	fmt.Println(proxyinfo)
	ip := proxyinfo["ip"].(string)
	port := int(proxyinfo["port"].(float64))
	// version := proxyinfo["version"].(int)
	// username := proxyinfo["username"].(string)
	// password := proxyinfo["password"].(string)
	addressProxy := fmt.Sprintf("%s:%d", ip, port)
	fmt.Println(addressProxy)
	dialer, err := proxy.SOCKS5("tcp", addressProxy, nil, proxy.Direct)
	if err != nil {
		// fmt.Fprintln(os.Stderr, "can't connect to the proxy:", err)
		return "Error"
	}
	httpTransport := &http.Transport{}
	httpClient := &http.Client{Transport: httpTransport}

	httpTransport.Dial = dialer.Dial

	req, err := http.NewRequest("GET", URL, nil)
	if err != nil {
		// fmt.Fprintln(os.Stderr, "can't create request:", err)
		return "Error"
	}

	resp, err := httpClient.Do(req)
	if err != nil {
		// fmt.Fprintln(os.Stderr, "can't GET page:", err)
		return "Error"
	}
	defer resp.Body.Close()
	b, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		// fmt.Fprintln(os.Stderr, "error reading body:", err)
		return "Error"
	}
	result := string(b)
	return result
}
