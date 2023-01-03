import urllib
import requests

import re
from scrapy.selector import Selector
from utils.TryRequest import *
import utils.broswer as ub
from utils.gearpack import *
# from scrapy.http import HtmlResponse

def search_google(query):
    # 爬取网页html源码
    query =  urllib.parse.quote(query)
    url = 'https://google.com/search?q=' + query
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
    # proxies = getproxies()
    while True:
        try:
            # proxies  = getproxies()
            response = requests.get(url, headers=headers,proxies= getproxies()) #随机一个ip地址抓取
            if response.status_code==200:
                print("谷歌的数据抓到了")
                break
        except:
            print("出错了。。。")
            time.sleep(2)
    page = Selector(response=response)
    
    str =response.text
    ub.open_in_broswer(str) #用浏览器打开
    cards = page.css('.Gx5Zad.fP1Qef.xpd.EtOod.pkphOe')
    # cards = page.css('.Gx5Zad.EtOod.pkphOe')
    data_set = {}
    for card in cards:
        try:
            url = card.css('a::attr(href)').extract()[0]
            domain = find_domain(url)
            linked_url = find_link(url)#指向地址    
            title = card.css('.vvjwJb::text').extract()[0]
            content = card.css('.s3v9rd::text').extract_first()
            # print(url,title,content)
            data_set[domain] = [linked_url,title,content]
        except:
            pass

    cards = page.css('.Gx5Zad.xpd.EtOod.pkphOe')
    for card in cards:
        try:
            url = card.css('a::attr(href)').extract()[0]
            domain = find_domain(url)
            linked_url = find_link(url)#指向地址    
            title = card.css('.rQMQod.Xb5VRe::text').extract()[0]
            content = card.css('.BNeawe.s3v9rd.AP7Wnd::text').extract_first()
            # print(url,title,content)
            data_set[domain] = [linked_url,title,content]
        
        except:
            pass

    # print(data_set)
    return data_set


if __name__ == '__main__':
    # results = search_google(query='2G-ENGINEERING')
    query = "ibm email format"
    results = search_google(query=query)
    print(results)
