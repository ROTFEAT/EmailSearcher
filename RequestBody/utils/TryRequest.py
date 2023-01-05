import requests
import time
# class Utils():
def trypost(url,cookies,headers,json):
    while 1:
        try:
            a = [cookies,headers,json]
            response = requests.post(url,cookies=cookies, headers=headers, json=json)
            a = 1
            if (response.status_code ==200)|(response.status_code ==201):
                break
            
        except:
            print("爬虫被发现了 休息一下zzzzz")
            time.sleep(2)
    
    return response

def tryget(url,params,cookies,headers):
    while 1:
        try:
            
            response = requests.get(url,params=params, cookies=cookies, headers=headers)
            a = 1
            if response.status_code ==200:
                break
            
        except:
            print("爬虫被发现了 休息一下zzzzz")

            time.sleep(2)
    
    return response

def getip():
    url =  "http://192.168.1.10:8000/utils/get_proxy_ip"
    ip = requests.get(url).json()
    # proxies = { "http": ip} 
    return ip

def getproxies():
    url =  "http://192.168.1.10:8000/utils/get_proxy_ip"
    ip = requests.get(url).json()
    proxies = { "http": ip} 
    return proxies

def getmyip(proxies=None):
    url = "http://httpbin.org/ip"
    if proxies: 
        proxies = proxies
    else:
        proxies=getproxies()  
    myip = requests.get(url,proxies=proxies).json()
    print("抓到的ip地址：",proxies)
    print("实际的ip地址：",myip)
    return myip

if __name__ =="__main__":
    pro = getproxies()
    a = getmyip(pro)
    # print(a)
    # ip,proxies = getip()
    # print(getip())