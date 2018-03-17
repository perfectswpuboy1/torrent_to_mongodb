# -*- coding: utf-8 -*-
#!/usr/bin/env python

# 《Torrent magnet存入数据库思路》
'''
    # 1.利用python字符串处理函数获取唯一✅标识，（先尝试是否可以手动增加_id进去）
    # 2.每次保存数据之前，先搜索数据库，确保没有重复，然后再保存。
    # 3.保存字段有：【文件名、文件大小、链接、时间、关键标识】
    # 4.file_name0  filesize0   magnet0  datetime0  keywords0
    # 5.
'''
import pymongo             #导入pymongo模块         。PS：让py2.7安装pymongo的命令是 pip2 install  ,相应的让3安装就是pip3 install
import datetime            #导入时间模块
import re

def get_db():
    # 建立连接
    client = pymongo.MongoClient(host="127.0.0.1", port=27017)  #设置主机地址和端口，建立数据库链接。
    db = client['torrentkitty']                                      #或者使用字典的方式获取链接。
    #或者 db = client.example                                    #获取属性的方式
    return db  #返回获取到的数据库

def get_collection(db):
    # 选择集合（mongo中collection和database都是延时创建的）
    coll = db['informations']       #选择这个集合。多个document的合体，就是集合。
    #print db.collection_names()     #打印集合名字
    return coll                     #返回集合

def insert_one_doc(db,file_name0,filesize0,magnet0):
    # 插入一个document               #mongodb中每一条信息叫document
    coll = db['informations']       #选择这个集合
    #step1 获取magnet链接的keyid   21-61位为关键字串   [20:61]
    keywords0=magnet0[20:60]
    #step2 查找keywords0是否重复。
    if coll.find_one({"Vedio_KeyID": keywords0}) == None:
        print "数据库中没有该文件。Will Add to the database!"
        information = {"Vedio_name": file_name0, "File_size": filesize0, "Magnet_Link": magnet0,
                       "Save_Time": datetime.datetime.utcnow(), "Vedio_KeyID": keywords0}  # 字典，准备插入的字典。
        information_id = coll.insert(information)  # 插入这一条字典，获取
        print information_id
    else:
        print "数据库已经有该文件。忽略!"
        pass
        #print "else"

def get_many_docs(db,find_key):
    # mongo中提供了过滤查找的方法，可以通过各种条件筛选来获取数据集，还可以对数据进行计数，排序等处理
    coll = db['informations']
    #ASCENDING = 1 升序;DESCENDING = -1降序;default is ASCENDING
    item_list=[]
    for item in coll.find({"Vedio_name":re.compile(find_key)}).sort("Vedio_name", pymongo.DESCENDING):
        print item
        item_list.append(item)

    count = coll.count()
    print "集合中所有数据 %s个" % int(count)
    return item_list

    #条件查询
    #count = coll.find({"name":"quyang"}).count()
    #print "quyang: %s"%count


if __name__ == '__main__':
    print "Please use it by import!"
    db = get_db()  # 建立链接
    my_collection = get_collection(db)  # 获取集合
    post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}  # 设置需要插入的内容，为一个字典。
    # 插入记录
    my_collection.insert(post)  # 插入上面的字典
    print my_collection.find_one({"x": "10"})
    information = {"name": "quyang", "age": "25"}     #字典，准备插入的字典。
    information_id = my_collection.insert(information)         #插入这一条字典，获取
    print information_id