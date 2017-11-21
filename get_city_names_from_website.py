
#!/usr/bin/python
# coding: utf-8

from bs4 import BeautifulSoup
import urllib2

url = "http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201703/t20170310_1471429.html" # 目标 url
headers = { 'User-Agent':'Mozilla/5.0' } # 设置 headers
request = urllib2.Request(url, headers = headers) 
response = urllib2.urlopen(request)
pages = response.read()
soup = BeautifulSoup(pages, 'lxml')
tag_span = soup.find_all('span', attrs={'style': 'font-family: 宋体'}) # 找到城市名所在的 tag

city_names = []
for name in tag_span:
    if name.string[-1] == u'市': # 仅保留市级城市名，并存储在列表中
        city_names.append(name.string[:-1].strip())

city_names_text = open('city_names.txt', 'w') # 将城市名存储在 txt 文件中
for city in city_names:
    city_names_text.write(city.encode('utf-8'))
    city_names_text.write('\n')
city_names_text.close()

