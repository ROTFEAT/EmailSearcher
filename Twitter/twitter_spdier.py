from Selenium.S_Spider_Base import *
from Twitter.twitter import inert2twitter
from Twitter.breached_twitter import query_email
class Twitter_spider(BaseSpider):
# "css-18t94o4 css-1dbjc4n r-1ny4l3l r-ymttw5 r-1f1sjgu r-o7ynqc r-6416eg"
    count = 0
    def getfollowers(self):
        self.GetPage()
        # cards = self.page.css('.css-18t94o4.css-1dbjc4n.r-1ny4l3l.r-ymttw5.r-1f1sjgu.r-o7ynqc.r-6416eg')
        cards = self.page.css('[data-testid = "UserCell"]')[-100:]
        source = self.source
        for card in cards:
            name = card.css(".css-901oao.css-16my406.css-1hf3ou5.r-poiln3.r-bcqeeo.r-qvutc0 span::text").get()
            url = card.css(".css-901oao.css-1hf3ou5.r-1bwzh9t.r-18u37iz.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-qvutc0 span::text").get()
            content = card.css('.css-901oao.r-1nao33i.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-1h8ys4a.r-1jeg54m.r-qvutc0').get()
            content = htmlfilter(content)
            email = emailfilter(content)
            email_str = list2str(email)
            breached_email = ""
            # try:
            #     breached_email = query_email(url)
            # except:
            #     breached_email = ""
            # 入库
            res =inert2twitter(name = name,url=url,breached_email=breached_email,content_email=email_str,content=content,source=source)
            if res:
                self.count+=1
                print("抓取了：",self.count,"个账号")
                
            # number = (name,url,content,email)
            # print(number)

    def setsource(self,source):
        self.source = source
    
    # def 

from selenium.webdriver.common.keys import Keys

if __name__ =="__main__":
    url = "https://www.twitter.com/"
    target_urls  = [
        # "https://twitter.com/fictiv",
        # "https://twitter.com/QuickpartsMFG",
        # "https://twitter.com/3erapid",
        # "https://twitter.com/HLHPrototypes",
        # "https://twitter.com/fathommfg",
        # "https://twitter.com/craftcloud3d",
        # "https://twitter.com/sculpteo",
        # "https://twitter.com/wikifactory",
        # "https://twitter.com/useplyable",
        "https://twitter.com/SuNPe_PROTOTYPE",
        "https://twitter.com/Rapidmade",
        "https://twitter.com/prismier",
        "https://twitter.com/ProtocaseInc",
        "https://twitter.com/ENSCO_Inc",
        "https://twitter.com/Prototek",
        ]
    for target_url in target_urls:
        foll_url = target_url+"/followers"
        # following_url = "https://twitter.com/HubsMFG/following"
        source = foll_url.replace("https://twitter.com/","").replace("/followers","")
        twitter_spider = Twitter_spider(url)
        cookie_file_path = "twitter/twitter.json"
        twitter_spider.useCookie(cookie_path=cookie_file_path,url = foll_url)
        twitter_spider.setsource(source=source)#设置数据来源
        twitter_spider.broswer.minimize_window()
        while True:
            twitter_spider.getfollowers()
            twitter_spider.broswer.execute_script('window.scrollBy(0,600)')

            if twitter_spider.isthatButtom():#如果是底部 就退出
                print('已经到底部了 浏览器退出')
                break
            # hight = twitter_spider.broswer.execute_script('return document.body.scrollHeight')
            # hight2 = twitter_spider.broswer.execute_script('return document.documentElement.scrollHeight')
            
            time.sleep(1)
        
        
    