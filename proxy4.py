#encoding=utf8
import urllib2
import BeautifulSoup
import random
from multiprocessing.dummy import Pool
def proxys():
    proxy_cont=open("/Users/linsange/proxy").read()
    ##proxy_avi是经过测试可用的代理服务器
    proxy_list=proxy_cont.split('\n')
    return proxy_list

def crawl_ip(page):
    print page
    User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
    header = {}
    header['User-Agent'] = User_Agent

    for proxy in proxys():
        proxy={"http":proxy}
        proxy_support = urllib2.ProxyHandler(proxy)  # 注册代理
        # opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler(debuglevel=1))  ##构建open
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)

        url = 'http://www.xicidaili.com/nn/' + str(page)
        req = urllib2.Request(url, headers=header)
        try:
            response = urllib2.urlopen(req, None,5)
            soup = BeautifulSoup.BeautifulSoup(response)
            ips = soup.findAll('tr')
        except Exception as e:
            continue

        with open("proxy.txt",'a+') as f:
            for x in range(1,len(ips)):
                ip = ips[x]
                tds = ip.findAll("td")
                ip_temp = tds[1].contents[0]+"\t"+tds[2].contents[0]+"\n"
                # print ip_temp
                # print tds[2].contents[0]+"\t"+tds[3].contents[0]
                f.write(ip_temp)
        print "final"
        break


if __name__=="__main__":
    pagelist=range(298,1011)
    pool=Pool(8)
    pool.map(crawl_ip,pagelist)
    pool.close()
    pool.join()
