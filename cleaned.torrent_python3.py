# -*- coding: utf-8 -*-
# For python3 is ok for torrentkitty

'''
For python2 test.因为pyopenssl是老版本，且非常不好升级，使出了浑身解数也无济于事，所以现在用python3将之前的代码重写一遍。
'''


import ssl
ssl._create_default_https_context = ssl._create_unverified_context #关闭https协议验证证书

import os
os.environ['http_proxy'] = 'http://127.0.0.1:1087'
os.environ['https_proxy'] = 'https://127.0.0.1:1087'





#proxies = {"http": "127.0.0.1:1087", "https": "127.0.0.1:1087"}

#header={'User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}


url1='https://www.torrentkitty.tv/search/AIKI/1' #error for python2,but ok for pyton3



#m = requests.get(url,proxies=proxies)

#m = requests.get(url) #如果没有代理，将无法访问。

#print( m.content )  # youtube is ok,But torrentkitty is not ok!

'''
Python3 urllib学习
'''

import urllib.request


#url = "http://tieba.baidu.com"

#response = urllib.request.urlopen(url,timeout=5)  #不足以构成一个完整的请求。
#html = response.read()         # 获取到页面的源代码
#print(html.decode('utf-8'))    # 转化为 utf-8 编码


#url = "http://tieba.baidu.com/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
request = urllib.request.Request(url=url1, headers=headers)  #这是一个完整的请求。
'''
使用 Request 伪装成浏览器发起 HTTP 请求。如果不设置 headers 中的 User-Agent，默认的User-Agent是Python-urllib/3.5。
可能一些网站会将该请求拦截，所以需要伪装一下。

'''


response = urllib.request.urlopen(request)


print(response.read().decode('utf-8'))



