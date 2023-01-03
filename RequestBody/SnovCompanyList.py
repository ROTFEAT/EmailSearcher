import requests
from utils.TryRequest import *
import os
import sys
# sys.path.append("C:\公司项目\爬虫\snov_fake")
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "."))) #导入当前目录
from SnovBaseRequestBody import SnovBaseRequestBody
class Companylist(SnovBaseRequestBody):
    cookies = {
    'snovTrackingId': 'jzrUnINGUvpXtOGwPzoG8sYo4yNzlyUM50U6q9zbWnlDybqW0KfZccc270BVZJEB',
    '_gcl_au': '1.1.1271293594.1664270831',
    '_ga': 'GA1.3.654970337.1664270832',
    'snovTrackingId': 'jzrUnINGUvpXtOGwPzoG8sYo4yNzlyUM50U6q9zbWnlDybqW0KfZccc270BVZJEB',
    '_hjSessionUser_915836': 'eyJpZCI6Ijc0MzdkMzdiLTZmOGYtNTg1YS1hNzAxLTViN2VkOTRmYTEzYiIsImNyZWF0ZWQiOjE2NjQyNzA4MzI1NDgsImV4aXN0aW5nIjp0cnVlfQ==',
    'psuid': 'e2e845b3-8efc-4cd4-8a91-2afe3d5f325d',
    'userId': '04344882792afc5e98425d82bb6895e7932c616539bd3fd1fd455c4082bc7858',
    'lang': 'eyJpdiI6ImM2TGhYWmNvQ3VDUGRpR0h2bVNHQUE9PSIsInZhbHVlIjoic0VocmgyQ1FcL3JXR29La3lHOEFVUWc9PSIsIm1hYyI6IjMwZjI4MjM1MWE2Nzg0ODllYjA5ZDExMGExNGEzZjUxODM3NjczZGQ3OTVmYjU1MTY5NjIzNjhhZWY0YTBhNjYifQ%3D%3D',
    'Hm_lvt_37b39b5356e9556531e38d50ddd8c555': '1668769217,1669454806,1669625334,1669865201',
    'tz': 'Etc/GMT-8 %2B08%3A00',
    '_gid': 'GA1.3.131516366.1671088401',
    '_ga': 'GA1.1.654970337.1664270832',
    '_hjIncludedInSessionSample': '0',
    '_hjSession_915836': 'eyJpZCI6IjhmMjRkZjFjLTIxNzItNDJiNi1iMzliLWJiNWJlNWU2MGI0MyIsImNyZWF0ZWQiOjE2NzEyNTcxMTYyMzUsImluU2FtcGxlIjpmYWxzZX0=',
    'crisp-client%2Fsession%2Fa8acb4a0-a13f-4d09-b433-ea92cabf4252': 'session_3f0b6dba-d64e-4769-a5db-bb7088193152',
    'token': '70d9594c8b7ece4146dbc8514791b204',
    'selector': 'a42070e3c4ae291da26a41f89fba3750',
    'snov_io': 'dLjJqLl2P4u2y1rb8EaknE4BaoiZnL5CUYwswgVH',
    'st_ua': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NzEyODU5MjQsImRhdGEiOnsidXNlciI6eyJpZCI6MTg4MjA0NCwiZW1haWwiOiJodWFqaWFubW9iaWxlQGdtYWlsLmNvbSIsIm5hbWUiOiJKaWFuIEppYW4iLCJjb3VudHJ5IjoiQ04iLCJsYW5nIjoiemgiLCJzZXNzaW9uU3RhcnRlZEF0TXMiOjE2NzEyNTcxMjQ0NjksImN1cnJlbmN5SWQiOjEsInRpbWV6b25lIjoiQXNpYVwvU2hhbmdoYWkiLCJ0ZWFtIjp7ImlzTGVhZCI6MH19fX0.kFwo9JK4P4V64PZD_K2Y2ETPtU9WspIG7_KNKgVmSJQ',
    'Hm_lpvt_37b39b5356e9556531e38d50ddd8c555': '1671257125',
    '_ga_BNRTCNFP5Y': 'GS1.1.1671257115.83.1.1671257142.33.0.0',
    'XSRF-TOKEN': 'eyJpdiI6ImRVbzF2SFNhRDQramwzZEp6dHlQUmc9PSIsInZhbHVlIjoiSHJSTHVKbENoZWNJN24yNkZnUXBNNmZYTkZPUWd5UDAzTlhXZlwveTZidzBZNTJ0b2FBYUoyNktlb0pxT29UamZGYXpmZVJEYjVBbWpXQTZ5VGxRc0t3PT0iLCJtYWMiOiJjZmM2NDk2ZGUxYTgxYWUzODBlOTFhOGRiOGRmYmE0OGI5ZTA5YjM5NWVhMTZkM2RjNzUzZWNhNDEyZWMyY2MyIn0%3D',
}

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ja;q=0.6,et;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'snovTrackingId=jzrUnINGUvpXtOGwPzoG8sYo4yNzlyUM50U6q9zbWnlDybqW0KfZccc270BVZJEB; _gcl_au=1.1.1271293594.1664270831; _ga=GA1.3.654970337.1664270832; snovTrackingId=jzrUnINGUvpXtOGwPzoG8sYo4yNzlyUM50U6q9zbWnlDybqW0KfZccc270BVZJEB; _hjSessionUser_915836=eyJpZCI6Ijc0MzdkMzdiLTZmOGYtNTg1YS1hNzAxLTViN2VkOTRmYTEzYiIsImNyZWF0ZWQiOjE2NjQyNzA4MzI1NDgsImV4aXN0aW5nIjp0cnVlfQ==; psuid=e2e845b3-8efc-4cd4-8a91-2afe3d5f325d; userId=04344882792afc5e98425d82bb6895e7932c616539bd3fd1fd455c4082bc7858; lang=eyJpdiI6ImM2TGhYWmNvQ3VDUGRpR0h2bVNHQUE9PSIsInZhbHVlIjoic0VocmgyQ1FcL3JXR29La3lHOEFVUWc9PSIsIm1hYyI6IjMwZjI4MjM1MWE2Nzg0ODllYjA5ZDExMGExNGEzZjUxODM3NjczZGQ3OTVmYjU1MTY5NjIzNjhhZWY0YTBhNjYifQ%3D%3D; Hm_lvt_37b39b5356e9556531e38d50ddd8c555=1668769217,1669454806,1669625334,1669865201; tz=Etc/GMT-8 %2B08%3A00; _gid=GA1.3.131516366.1671088401; _ga=GA1.1.654970337.1664270832; _hjIncludedInSessionSample=0; _hjSession_915836=eyJpZCI6IjhmMjRkZjFjLTIxNzItNDJiNi1iMzliLWJiNWJlNWU2MGI0MyIsImNyZWF0ZWQiOjE2NzEyNTcxMTYyMzUsImluU2FtcGxlIjpmYWxzZX0=; crisp-client%2Fsession%2Fa8acb4a0-a13f-4d09-b433-ea92cabf4252=session_3f0b6dba-d64e-4769-a5db-bb7088193152; token=70d9594c8b7ece4146dbc8514791b204; selector=a42070e3c4ae291da26a41f89fba3750; snov_io=dLjJqLl2P4u2y1rb8EaknE4BaoiZnL5CUYwswgVH; st_ua=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NzEyODU5MjQsImRhdGEiOnsidXNlciI6eyJpZCI6MTg4MjA0NCwiZW1haWwiOiJodWFqaWFubW9iaWxlQGdtYWlsLmNvbSIsIm5hbWUiOiJKaWFuIEppYW4iLCJjb3VudHJ5IjoiQ04iLCJsYW5nIjoiemgiLCJzZXNzaW9uU3RhcnRlZEF0TXMiOjE2NzEyNTcxMjQ0NjksImN1cnJlbmN5SWQiOjEsInRpbWV6b25lIjoiQXNpYVwvU2hhbmdoYWkiLCJ0ZWFtIjp7ImlzTGVhZCI6MH19fX0.kFwo9JK4P4V64PZD_K2Y2ETPtU9WspIG7_KNKgVmSJQ; Hm_lpvt_37b39b5356e9556531e38d50ddd8c555=1671257125; _ga_BNRTCNFP5Y=GS1.1.1671257115.83.1.1671257142.33.0.0; XSRF-TOKEN=eyJpdiI6ImRVbzF2SFNhRDQramwzZEp6dHlQUmc9PSIsInZhbHVlIjoiSHJSTHVKbENoZWNJN24yNkZnUXBNNmZYTkZPUWd5UDAzTlhXZlwveTZidzBZNTJ0b2FBYUoyNktlb0pxT29UamZGYXpmZVJEYjVBbWpXQTZ5VGxRc0t3PT0iLCJtYWMiOiJjZmM2NDk2ZGUxYTgxYWUzODBlOTFhOGRiOGRmYmE0OGI5ZTA5YjM5NWVhMTZkM2RjNzUzZWNhNDEyZWMyY2MyIn0%3D',
        'DNT': '1',
        'Pragma': 'no-cache',
        'Referer': 'https://app.snov.io/database-search',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'X-CSRF-Token': 'F0QX9Pgwe9ZCtAY4ymnfufe8Ze2NrG5j9wylj4D9',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6ImRVbzF2SFNhRDQramwzZEp6dHlQUmc9PSIsInZhbHVlIjoiSHJSTHVKbENoZWNJN24yNkZnUXBNNmZYTkZPUWd5UDAzTlhXZlwveTZidzBZNTJ0b2FBYUoyNktlb0pxT29UamZGYXpmZVJEYjVBbWpXQTZ5VGxRc0t3PT0iLCJtYWMiOiJjZmM2NDk2ZGUxYTgxYWUzODBlOTFhOGRiOGRmYmE0OGI5ZTA5YjM5NWVhMTZkM2RjNzUzZWNhNDEyZWMyY2MyIn0=',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }



    params = {
        'taskId': '55356',
        'page': '0',
    }
    def setpage(self,page):
        self.params["page"]=str(page)

    def nextpage(self):
        self.params["page"]=self.params["page"] + 1 
    
    def settaskid(self,id):
        self.params["taskId"] = str(id)
    
    def getcompanylist(self):
        url = "https://app.snov.io/new/company-profile-search/result"
        print("=========================")
        print(url,self.params)
        print("=========================")
        response = tryget(url,params=self.params, cookies=self.cookies, headers=self.headers)
        # response = requests.get('https://app.snov.io/new/company-profile-search/result', params=self.params, cookies=self.cookies, headers=self.headers)
        return response
