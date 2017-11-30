import requests
import html5lib
import re
from bs4 import BeautifulSoup
from lxml import etree

s=requests.Session()
for id in range(0,251,25):
    url='https://movie.douban.com/top250?start=' + str(id)
    r=s.get(url)
    r.encoding='utf-8'
    root=etree.HTML(r.content)
    items=root.xpath('//ol/li/div[@class="item"]')
    for item in items:
        title=item.xpath('./div[@class="info"]//a/span[@class="title"]/text()')
        name=title[0].encode('gb2312','ignore').decode('gb2312')
        rating=item.xpath('//*[@id="content"]/div/div[1]/ol/li[10]/div/div[2]/div[2]/div/span[2]/text()')[0]

        #rating=item.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]
        print(name,rating)
