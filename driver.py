# coding=utf-8
# author by violinxsc
from selenium import webdriver
import time
import re
from pyquery import PyQuery as pq


def openUrl(url, num=0):
    browser = webdriver.Chrome()  # 打开浏览器
    time.sleep(2)
    print("浏览器最大化")
    browser.maximize_window()  # 将浏览器最大化显示
    browser.get(url)  # 进入相关网站
    html = browser.page_source  # 获取网站源码
    data = str(pq(html))  # str() 函数将对象转化为适于人阅读的形式。
    time.sleep(3)
    browser.find_element_by_class_name("userinfo-loginBtn-20a9e").click()
    time.sleep(1)
    html = browser.page_source
    data = str(pq(html))
    return data


url = 'https://yuba.douyu.com/p/943673931545027287'
data = openUrl(url)
data.encode('utf8')
# print(data)
f = open("D:\\python\\project\\html.txt", "w", encoding='utf-8')
f.write(data)
f.close()
