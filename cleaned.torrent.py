# -*- coding: utf-8 -*-

import urllib2
import urllib
from lxml import etree

import codecs
import requests
from bs4 import BeautifulSoup
import pymongo_imp

search_list=['keyword1','keyword2']   #这里建立一个关键字列表，一次性把想要搜索的内容全部搜索一遍，解放你的双手和眼睛。
for keys2x in search_list:

    url = 'https://www.torrentkitty.tv/search/'
#    keys2x = raw_input("请输入搜索关键字：")
    keyword = urllib.quote(keys2x)  # 这是python2的语法
    pages = 30
    file_name = '/Users/llm/PycharmProjects/' + keys2x + '.txt'
    ks = file_name
    for page in range(0, pages):
        page = str(page)
        print "当前页码：%s" % page

        site = url + keyword + '/' + page

        h = urllib2.Request(site)  ###

        h.add_header('User-Agent',
                 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14')

        try:      #引入异常处理机制
            ht = urllib2.urlopen(h)     #网页请求
         

            html = ht.read(ht)
            soup = BeautifulSoup(html, "lxml")                                              #####>>>>>>1     创建美丽汤。
            movie_list_soup = soup.find('table', attrs={'id': 'archiveResult'})             #####>>>>>>2     定位到列表所在位置。#archiveResult
            movie_name_list = []                                                            #####>>>>>>3     新建列表，存放查找内容。
            search_flag=0
            for movie_li in movie_list_soup.find_all('tr'):                                 #####>>>>>>4     设置过滤器。找到所有tr标签。
                search_flag=search_flag+1
                if search_flag > 1:                                                         #####>>>>>>4.1   设置查找标志，跳过第一个，因为第一个是表头。
                    detail = movie_li.find('td', attrs={'class': 'size'}).getText()         #####>>>>>>5     定位所有的size标签，得到字符串。
            #上面获取了文件大小。
            #print "%s \n" % detail
                    if movie_li.find('a', attrs={'rel': 'magnet'}) is None:
                        pass
                    else:
                        detail_name1 = movie_li.find('a', attrs={'rel': 'magnet'})['title']
                        FHD_flag=detail_name1.find('FHD')
                        Thz_flag=detail_name1.find('Thz.la')
                    if FHD_flag<>-1 or Thz_flag<>-1:                                         #####>>>>>>5.1     如果是高清或者是tha.lz那么就存档。
            ##if detail.find('mb')<>-1:                                               #####>>>>>>6     如果文件大小满足要求，那么下一步寻找兄弟节点。
                #文件名称
                        if movie_li.find('a', attrs={'rel': 'magnet'}) is None:
                            pass
                        else:
                            detail_name=movie_li.find('a', attrs={'rel': 'magnet'})['title']
                    #上面获取了文件名称。❕
                            print detail_name
                # 文件大小  detail
                        print detail
                #链接地址
                        file_name = ks + '_' + page  # 让文件按页码保存，避免一个文件中链接数量太多。
                        if movie_li.find('a', attrs={'rel': 'magnet'}) is None:                ####>>>>>>>      如果为非空，那么就获取。
                            pass
                        else:
                            detail_mag=movie_li.find('a', attrs={'rel': 'magnet'})['href']      #####>>>>>>7     获取磁力链接地址。
                    #上面获取了磁力链接。❕
                            print detail_mag
                    #with open(file_name, 'a') as p:  # '''Note'''：Ａppend mode, run only once!
                    #    p.write("%s \n \n" % detail_mag)  ##!!encode here to utf-8 to avoid encoding

                    #获取了磁力链接之后开始存入数据库。
                            print "开始进行mongodb数据库操作:"
                    #存入数据库
                            db=pymongo_imp.get_db()
                            my_collection = pymongo_imp.get_collection(db)

                            pymongo_imp.insert_one_doc(db,detail_name,detail,detail_mag)

                            print "截止目前，数据库中存放条目数量：%s个" % int(my_collection.count())

        except:
            pass