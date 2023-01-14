from Selenium.S_Spider_Base import *
from Twitter.twitter import inert2twitter
from Twitter.breached_twitter import query_email
class Twitter_spider(BaseSpider):
# "css-18t94o4 css-1dbjc4n r-1ny4l3l r-ymttw5 r-1f1sjgu r-o7ynqc r-6416eg"

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
            inert2twitter(name = name,url=url,breached_email=breached_email,content_email=email_str,content=content,source=source)

            # number = (name,url,content,email)
            # print(number)

    def setsource(self,source):
        self.source = source

from selenium.webdriver.common.keys import Keys

if __name__ =="__main__":
    url = "https://www.twitter.com/"
    foll_url = "https://twitter.com/RAPIDDIRECT1/followers"
    # following_url = "https://twitter.com/HubsMFG/following"
    source = foll_url.replace("https://twitter.com/","").replace("/followers","")
    twitter_spider = Twitter_spider(url)
    cookie_file_path = "twitter/twitter.json"
    twitter_spider.useCookie(cookie_path=cookie_file_path,url = foll_url)
    twitter_spider.setsource(source=source)#设置数据来源
    while True:
        twitter_spider.getfollowers()
        twitter_spider.broswer.execute_script('window.scrollBy(0,600)')
        time.sleep(1)
        
    