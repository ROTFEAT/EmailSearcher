from Selenium.S_Spider_Base import *
from selenium.webdriver.common.keys import Keys
class xoSelnium(BaseSpider):

    
    def getindex(self):
        
        # s1 = Select(self.broswer.find_element_by_id('s1Id'))
        s1 = self.broswer.find_element(by=By.XPATH,value='//*[@id="s1Id"]')
        s1.get_attribute()
                # pass
    
    def downlist(self):
        ActionChains(self.broswer)\
        .key_down(Keys.DOWN)\
        .perform()


    def enter(self):
        ActionChains(self.broswer)\
        .key_down(Keys.ENTER)\
        .perform()

    def getnumberofProcess(self):
        self.GetPage()
        num = self.page.css('.css-dz7869-menu div').extract()
        num = len(num)
        return num


    def touchProcess(self):
        self.broswer.find_element(by=By.XPATH,value='//*[@id="process-selector-select-component"]/div/div[1]').click()


    def getProcess(self):
        self.GetPage()
        value = self.page.css('#process-selector-select-component .css-1uccc91-singleValue::text').extract_first()
        return value
        # pass
# "css-dz7869-menu"

    def getmaterial(self):
        self.GetPage()
        value = self.page.css('#material-select .css-1uccc91-singleValue::text').extract_first()
        return value
    
    def gettechnology(self):
        self.GetPage()
        value = self.page.css('#3d-printing-process-select .css-1uccc91-singleValue::text').extract_first()
        return value
        

    def getfinish(self):
        self.GetPage()
        value = self.page.css('#finish-binderjet-multiselect .css-1uccc91-singleValue::text').get()
        value2 = self.page.css('#finish-multiselect .css-1uccc91-singleValue::text')
        return value

    def gettolerance(self):
        self.GetPage()
        value = self.page.css('#tolerance-select-metals .css-1uccc91-singleValue::text').extract_first()
        return value
        
    def getroughness(self):
        self.GetPage()
        value = self.page.css('#surface-roughness-select .css-1uccc91-singleValue::text').extract_first()
        return value
    
    def getValueOnthePage(self):
        process = self.getProcess()
        try:
            technology = self.gettechnology()
        except:
            technology = ""
        material = self.getmaterial()
        finish = self.getfinish()
        try:
            roughness = self.getroughness()
        except:
            roughness = ""
        return{
            "process":process,
            "tech":technology,
            "material":material,
            "finish":finish,
            "roughness":roughness,
        } 
    

if __name__ == "__main__":
    url = "https://www.xometry.com" #reference
    url2 = "https://www.xometry.com/quoting/quote/Q36-0160-6252/63be19d4d54e146933b66919?initialTab=Configure"
    xo_spider = xoSelnium(url)
    xo_spider.useCookie(url=url2)
    time.sleep(10)
    xo_spider.touchProcess()#点击
    # time.sleep(2)
    count = 1


    # res = {}
    out = []
    
    while 1:
        xo_spider.GetPage()
        value = xo_spider.getValueOnthePage()
        
        out.append(value)
        #构造dict
        # process = value['process']
        # tech  = value['tech']
        # material  = value['material']
        # finish  = value['Zirblast']
        # roughness  = value['roughness']
        a  = input("等待输入")
        if a =="yes":
            res = {"output":out}
            with open("output.json","w") as f:
                json.dump(res,f)
        else:
            pass
        count = count+1


    

    # while 1:
    #     xo_spider.touchProcess()#点击

    # xo_spider.downlist()
    # xo_spider.downlist()
    # xo_spider.downlist()
    # xo_spider.enter()

    # finish = xo_spider.getfinish()
    
    # # for item in 
    # a1 = 1
    # xo_spider.touchProcess()
    # xo_spider
    
    

    # xo_spider.GetPage()

    # # xo_spider
    # # xo_spider.getindex()
    # while 1:
    #     time.sleep(2)