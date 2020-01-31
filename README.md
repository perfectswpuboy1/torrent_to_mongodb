# torrent_to_mongodb
此脚本用来搜索TorrentKitty上的种子文件并存放到数据库中，方便后续快速找到种子磁力链接。

##2020.1.31更新

因为之前是用python2编写的脚本，现在发现urllib2模块无法正常访问种子网站了。最近花了一些时间来用python3重写了代码。

#重要提示内容
 
 - python3相对于python2来讲部分模块有增减，之前的urllib、urllib2现在整合成了urllib模块，不过之前有的子模块，现在可能没有了。
 - python3的print函数要求一定要用括号括起来。
 - os.environ['http_proxy'] = 'http://127.0.0.1:1087'可以自动让urllib挂代理爬网站。这一点在网络上找了好几天才知道，哎！
 - urllib.error模块可以比较好的进行异常捕获。
 - 不光需要判断种子文件名还要判断种子磁力链接是不是在数据库中也没有才能保证数据不重复。
 - 新版本的mongodb对数据库的插入还有查询总数有新的语法推荐。
