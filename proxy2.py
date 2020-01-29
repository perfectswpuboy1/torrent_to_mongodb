#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:24:38 2020

@author: linsange
"""

# *-*coding:utf-8*-*
from urllib import request
def use_porxy(porxy_addr,url):
    porxy = request.ProxyHandler({'http':porxy_addr})
    opener = request.build_opener(porxy, request.ProxyHandler)
    request.install_opener(opener)
    data = request.urlopen(url).read().decode('utf-8')
    return data
data = use_porxy("127.0.0.1:1087","https://twitter.com/")

print(len(data))