#encoding=utf8
import urllib2
import BeautifulSoup


#from bs4 import BeautifulSoup

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

url = 'http://www.xicidaili.com/nn/1'
req = urllib2.Request(url,headers=header)
res = urllib2.urlopen(req).read()

soup = BeautifulSoup.BeautifulSoup(res)
ips = soup.findAll('tr')
f = open("/Users/linsange/proxy","w")

for x in range(1,len(ips)):
    ip = ips[x]
    tds = ip.findAll("td")
    ip_temp = tds[2].contents[0]+"\t"+tds[3].contents[0]+"\n"
    # print tds[2].contents[0]+"\t"+tds[3].contents[0]
    f.write(ip_temp)