from Selenium.S_Spider_Base import *
from selenium.webdriver.common.keys import Keys
class xoSelnium(BaseSpider):
    def getvalues(self):
        self.GetPage()
        
        # form = self.page.css('.css-1pqfrpo.e1wfvszv0')
        # form = form.css('.css-js7wpr div:nth-of-type(3)+div+div div')
        # form  = self.page.xpath('//*[@id="metal-3d-printing"]/div')
        form  = self.page.xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div')
        res = {}
        for item in form:
            tag = item.css('.css-th66cq.ean5z2w0::text').get()
            value = item.css('.css-1uccc91-singleValue::text').get()
            if (tag!=None)&(value!=None):
                res[tag] = value
        print(res)
        return res
    

from functools import reduce 
def list2tree(list):
    res = reduce(lambda x, y: {y: x}, reversed(list), {})
    return res

def data2dic(data):#转为嵌套结构
    dic_list = []
    for key,value in data.items():
        
        dic_list.append(key)
        dic_list.append(value)

    new_dict  = list2tree(dic_list)
    return  new_dict


def dic2tree(dic,result):
    #输入dict 转为 tree 
    # result
    it = result
    dic_list = []
    for key,value in dic.items():
        
        dic_list.append(key)
        dic_list.append(value)

    new_dict  = list2tree(dic_list)
    # dic = dict(it, **new_dict)
    dict_update(result,new_dict)
    # result = dic
    # return result

def dict_update(raw, new):
    dict_update_iter(raw, new)
    dict_add(raw, new)
 
 
def dict_update_iter(raw, new):
    for key in raw:
        if key not in new.keys():
            continue
        if isinstance(raw[key], dict) and isinstance(new[key], dict):
            dict_update(raw[key], new[key])
        else:
            raw[key] = new[key]
 
 
def dict_add(raw, new):
    update_dict = {}
    for key in new:
        if key not in raw.keys():
            update_dict[key] = new[key]
 
    raw.update(update_dict)

import json
import win32con, ctypes, ctypes.wintypes
import win32api #pip install pypiwin32
if __name__ == "__main__":
    url = "https://www.xometry.com" #reference
    url2 = "https://www.xometry.com/quoting/quote/Q36-0160-6252/63be19d4d54e146933b66919?initialTab=Configure"
    xo_spider = xoSelnium(url)
    cookie_path = 'Xometory/cookies.json'
    xo_spider.useCookie(url=url2,cookie_path=cookie_path)
    time.sleep(10)
    # xo_spider.touchProcess()#点击
    # time.sleep(2)
    count = 1
    res = {}
    def esc_pressed():
        print("f2 was pressed.")

    ctypes.windll.user32.RegisterHotKey(None, 1, 0, win32con.VK_F2)#vk 注册f2
    try:

        msg = ctypes.wintypes.MSG()
        while ctypes.windll.user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
            if msg.message == win32con.WM_HOTKEY:

                data = xo_spider.getvalues() #返回页面数据
                
                new_data= data2dic(data=data)
                if (len(res)==0):              
                    # new = data2dic(data=data)
                    res = new_data
                
                dict_update(res,new_data)
                json_data = json.dumps(res)
                with open("3d-print.json","w") as f:
                    f.write(json.dumps(res))
                # print(res)
            

            ctypes.windll.user32.TranslateMessage(ctypes.byref(msg))
            ctypes.windll.user32.DispatchMessageA(ctypes.byref(msg))


    finally:
        ctypes.windll.user32.UnregisterHotKey(None, 1)
