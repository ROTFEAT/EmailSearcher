from optparse import Values
import re
import time
import atexit
from lxml.html import Element
# from numpy import short, sort
from scrapy.selector import  Selector
from scrapy.utils.trackref import NoneType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import threading
import json
import socket
import sys
# import Value

# from SQL_INSERT import  *

# from socket_test import *
# from SQLinsert import  *
# from PageSeletor import  *

Use_Socket = False


class BaseSpider():
    broswer = None
    t_span = 10 #刷新间隔
    oldContent = None
    oldGift = None
    page = None
    NewEnter = -1
    CapEnter = -1
    url = None
    def __init__(self,req_url):
        chromedriver_path = r"chromedriver.exe"
        chrome_options = Options()
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--profile-directory=Default')
        # chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument('--headless') #无窗口模式
        # chrome_options.binary_location = r"ChromePortable64\GoogleChromePortable.exe" #使用特定的chrome
        broswer =webdriver.Chrome(options=chrome_options,executable_path = chromedriver_path)
        # broswer.set_page_load_timeout(5)
        self.url = req_url
        while True:
            try:
                broswer.get(req_url)
                break
            except:
                time.sleep(5)
                print("请求出错：等待刷新")
                pass
        # self.broswer.maximize_window()
        self.url = req_url
        self.broswer = broswer

        #broswer就是通常的driver
    def useCookie(self,cookie_path,url = None):


        # cookie_path  = 'xometory/cookies.json' 路径举例
        try:
            self.broswer.delete_all_cookies()
        except:
            pass
        # cookiespath = ""
        with open(cookie_path, 'r', encoding='utf-8') as f:
            listCookies = json.loads(f.read())

        # cooklist =[]
        for cookie in listCookies:
            cookies = {'domain': cookie['domain'],
                    'name': cookie['name'],
                    'value': cookie['value'],
                    'path': '/',
                    'expires': None
                    }
            self.broswer.add_cookie(cookies)
        if url == None:
            self.broswer.get(self.url)
        else:
            self.broswer.get(url)
        a = 1

    def getcookies(self,cookie_path):
        cookies = self.browser.get_cookies()
        jsonCookies = json.dumps(cookies)
        with open('cookies.json', 'w') as f:
            f.write(jsonCookies)


    def GetPage(self):
        self.page = Selector(text=self.broswer.page_source)

    def Fliter(self,old):#测试Fliter
        return old

    def restruct(self,NEWdanmu):
        return NEWdanmu
    
    def CloseBroswer(self):
        self.broswer.close()
    
    def nextpage(self):
        pass

    def getelement(self):
        self.GetPage()
        # MessageId = self.page.css()  #范例
        userid = self.page.css('.chat-item.danmaku-item::attr(data-uid)').extract()
        MessageId = self.page.css('.chat-item.danmaku-item::attr(data-ts)').extract()
        SenderName = self.page.css('.chat-item.danmaku-item::attr(data-uname)').extract()
        SenderContent = self.page.css('.chat-item.danmaku-item::attr(data-danmaku)').extract()
    

def htmlfilter(raw_str):
    try:
        reg = re.compile('<[^>]*>')
        res = reg.sub('',raw_str)
        res.replace('\n',"") #去除空格
        return (res)
    except:
        return ""

def emailfilter(raw_str):
    try:   
        email_list = re.findall(r'([a-zA-Z0-9_.+-]+@[a-pr-zA-PRZ0-9-]+\.[a-zA-Z0-9-.]+)', raw_str)
        return email_list
    except:
        return []

def list2str(list):
      #有的题目要输出字符串，但是有时候list更好操作，于是可以最后list转string提交
    # list = ['1', '2', '3', '4', '5']
    res = ','.join(list) 
    return res 

    

if __name__ =="__main__":

    url = "https://www.twitter.com/"
    url = "https://twitter.com/Xometry/followers"
    broswer = BaseSpider(url)
    broswer.useCookie()
    while True:
        start = input("等待翻页:")
        broswer.GetPage()
        followers = broswer.page.css(".css-1dbjc4n.r-1adg3ll.r-1ny4l3l")
        for follower in followers:
            
            name = follower.page.css('.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')
            # name = follower.page.css('.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')
            
            #  follower.page.css('.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')
        time.sleep(2)

        
  
