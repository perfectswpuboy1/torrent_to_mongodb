# -*- coding: utf-8 -*-
# For python3 is ok for torrentkitty

'''
For python3 test.因为python2的pyopenssl是老版本，且非常不好升级，使出了浑身解数也无济于事，所以现在用python3将之前的代码重写一遍。
'''
'''
使用 Request 伪装成浏览器发起 HTTP 请求。如果不设置 headers 中的 User-Agent，默认的User-Agent是Python-urllib/3.5。
可能一些网站会将该请求拦截，所以需要伪装一下。

'''

import urllib.request
import ssl
import os
import pymongo             #导入pymongo模块         。
import datetime            #导入时间模块
import re
import urllib.error
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context #关闭https协议验证证书

os.environ['http_proxy'] = 'http://127.0.0.1:1087'
os.environ['https_proxy'] = 'https://127.0.0.1:1087'

def get_db():
    # 建立连接
    client = pymongo.MongoClient(host="127.0.0.1", port=27017)  #设置主机地址和端口，建立数据库链接。
    db = client['mongodb_bak']                                  #或者使用字典的方式获取链接。
    #或者 db = client.example                                    #获取属性的方式
    return db  #返回获取到的数据库

def get_collection(db):
    # 选择集合（mongo中collection和database都是延时创建的）
    coll = db['informations']        #选择这个集合。多个document的合体，就是集合。就是多个数据小条。
    #print db.collection_names()     #打印集合名字
    return coll                      #返回集合


def insert_one_doc(db,file_name0,filesize0,magnet0):
    '''
    这个设计之前是针对存入torrentkitty的，爬取softs需要重新设计。
    '''
    # 插入一个document               #mongodb中每一条信息叫document
    coll = db['informations']       #选择这个集合

    #step1 获取magnet链接的keyid   21-61位为关键字串   [20:61]

    keywords0=magnet0[20:60]
    #step2 查找keywords0是否重复。
    if coll.find_one({"Vedio_KeyID": keywords0}) == None:
        print ("数据库中没有该文件。Will Add to the database!")
        information = {"Vedio_name": file_name0, "File_size": filesize0, "Magnet_Link": magnet0,
                       "Save_Time": datetime.datetime.utcnow(), "Vedio_KeyID": keywords0}  # 字典，准备插入的字典。
        information_id = coll.insert(information)  # 插入这一条字典，获取
        print (information_id)
    else:
        print ("数据库已经有该文件。忽略!")
        pass
        #print "else"

def get_many_docs(db,find_key):
    # mongo中提供了过滤查找的方法，可以通过各种条件筛选来获取数据集，还可以对数据进行计数，排序等处理
    coll = db['informations']
    #ASCENDING = 1 升序;DESCENDING = -1降序;default is ASCENDING

    item_list=[]

    for item in coll.find({"Vedio_name":re.compile(find_key,re.I)}).sort("Vedio_name", pymongo.DESCENDING):
        print (item['Vedio_name'])
        print (item['Magnet_Link'])
        print ('\n-----------------------++++++++++++--------------------')

        item_list.append(item)

    #count = coll.count()


    find_strs = "查找到的数据有 %s 个" % len( item_list )
    print (find_strs)
    return item_list


#if __name__ == '__main__':
    # print "Please use it by import!"

#    db = get_db()  # 建立链接
#    get_many_docs( db, 'snis' )



#print(response.read().decode('utf-8'))      #获取请求的返回结果。


#-----------------------++++++++++++--------------------

search_list=['AIKA','SMBD']   #这里建立一个关键字列表，一次性把想要搜索的内容全部搜索一遍，解放你的双手和眼睛。
pages=1

url='https://www.torrentkitty.tv/search/' #error for python2,but ok for pyton3

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

resp_flag=0
for keys2x in search_list:
    for page in range(pages):
        page_str="当前页码：%s" %str(page+1) #简单处理，使得抓取页面跟pages相等。
        print (page_str)
        keyword=keys2x
        print (keyword)

        site=url + keyword + '/' + str(page+1)#简单处理，使得抓取页面跟pages相等。
        print (site)


        request = urllib.request.Request( url=site, headers=headers )  # Request是一个完整的请求。添加表头信息。
        try:
            response = urllib.request.urlopen( request )  # 正式发起请求
            html=response.read().decode('utf-8')
            resp_flag=1
        except urllib.error.HTTPError as e:
            print ( 'code: ' + e.code + '\n' )
            print ( 'reason: ' + e.reason + '\n' )
            print ( 'headers: ' + e.headers + '\n' )

        if resp_flag==1:
            soup=BeautifulSoup(html,"lxml")
            movie_list_soup=soup.find('table',attrs={'id':'archiveResult'})
            movie_name_list=[]
            search_flag=0
            for movie_li in movie_list_soup.find_all('tr'):
                search_flag += 1
                if search_flag > 1:
                    detail = movie_li.find('td',attrs={'class':'size'}).getText()
                    #print (detail)     #文件大小
                    if movie_li.find('a',attrs={'rel':'magnet'}) is None:
                        pass
                    else:
                        detail_name1=movie_li.find('a',attrs={'rel':'magnet'})['title']
                        #print ("nice")
                        FHD_flag=detail_name1.find('FHD')
                        THZ_flag=detail_name1.find('Thz.la')
                    







            pass













