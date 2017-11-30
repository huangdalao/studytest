'''
from bs4 import BeautifulSoup

import time
from selenium import webdriver

browser=webdriver.Chrome
browser.set_page_load_timeout(30)

#有多少页商品
browser.get('http://www.17huo.com/?mod=search&sq=2&keyword=%E7%94%B7%E8%A3%85&page=1')
page_info=browser.find_element_by_css_selector('body > div.wrap > div.pagem.product_list_pager > div')

#共 100 页，每页 24 条
pages=int((page_info.text.split(', ')[0]).split(' ')[1])
print('商品有%d页'% pages)
for i in range(pages):
    if i>4:
        break
    url='http://www.17huo.com/?mod=search&sq=2&keyword=%E7%94%B7%E8%A3%85&page='+str(i+1)
    browser.get(url)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(3)
    goods=browser.find_element_by_css_selector('body > div.wrap > div: nth - child(2) > div.p_main > ul').find_element_by_tag_name('li')
    print('第%d页有%d件商品' %((i+1),len(goods)))
    for good in goods:
        try:
            title=good.find_element_by_css_selector('a:nth-child(1) > p:nth-child(2)').text
            price=good.find_element_by_css_selector('div > a > span').text
            print(title,price)
        except:
            print(good.text)
'''

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.set_page_load_timeout(30)

browser.get('http://www.17huo.com/search.html?sq=2&keyword=%E7%BE%8A%E6%AF%9B')
page_info = browser.find_element_by_css_selector('body > div.wrap > div.pagem.product_list_pager > div')
# print(page_info.text)
pages = int((page_info.text.split('，')[0]).split(' ')[1])
for page in range(pages):
    if page > 2:
        break
    url = 'http://www.17huo.com/?mod=search&sq=2&keyword=%E7%BE%8A%E6%AF%9B&page=' + str(page + 1)
    browser.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)   # 不然会load不完整
    goods = browser.find_element_by_css_selector('body > div.wrap > div:nth-child(2) > div.p_main > ul').find_elements_by_tag_name('li')
    print('%d页有%d件商品' % ((page + 1), len(goods)))
    for good in goods:
        try:
            title = good.find_element_by_css_selector('a:nth-child(1) > p:nth-child(2)').text
            price = good.find_element_by_css_selector('div > a > span').text
            print(title, price)
        except:
            print(good.text)
