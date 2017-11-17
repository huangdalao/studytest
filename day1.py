import requests
import xml.etree.ElementTree as ET

def get_procince_entry(url):
    #开始
    content = requests.get(url).content.decode('gb2312')
    

provinces = get_procince_entry('http://www.ip138.com/post')
print(provinces)