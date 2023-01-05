
import os
import sys
# sys.path.append("C:\公司项目\爬虫\snov_fake")
# sys.path.append("C:\Code\Spider\request")
import json
# sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "."))) #导入当前目录
from RequestBody.utils.TryRequest import *
import difflib
from RequestBody.params import *
# from params import *
# from RequestsBody.utils.TryRequest import *
from RequestBody.utils.TryRequest import *
from RequestBody.SnovBaseRequestBody import  SnovBaseRequestBody
class Task(SnovBaseRequestBody):
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
    'XSRF-TOKEN': 'eyJpdiI6InY1NjhnQjFjb2puZTVDaWRcLytRU21RPT0iLCJ2YWx1ZSI6IlwvUm5IMEZ6UTAxK3R4Q3JvXC9DODBDQ3pWc1dPVXBHNDE1eTNqNEdNZzUxY2lPUTFGcmdNcFBGeFNQdGZGYktCRTNWWFwvQldnY01idHZDYVlBVDJ6aVNnPT0iLCJtYWMiOiI5MzQzYWI2ODAzOGUxMGViZDVjMDQwODk3ZjI1OThkNzJkYmQ2NmUyZWM5NmVhNGJhODgxZjg2MGU1OTQzYThmIn0%3D',
}

    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ja;q=0.6,et;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'snovTrackingId=jzrUnINGUvpXtOGwPzoG8sYo4yNzlyUM50U6q9zbWnlDybqW0KfZccc270BVZJEB; _gcl_au=1.1.1271293594.1664270831; _ga=GA1.3.654970337.1664270832; snovTrackingId=jzrUnINGUvpXtOGwPzoG8sYo4yNzlyUM50U6q9zbWnlDybqW0KfZccc270BVZJEB; _hjSessionUser_915836=eyJpZCI6Ijc0MzdkMzdiLTZmOGYtNTg1YS1hNzAxLTViN2VkOTRmYTEzYiIsImNyZWF0ZWQiOjE2NjQyNzA4MzI1NDgsImV4aXN0aW5nIjp0cnVlfQ==; psuid=e2e845b3-8efc-4cd4-8a91-2afe3d5f325d; userId=04344882792afc5e98425d82bb6895e7932c616539bd3fd1fd455c4082bc7858; lang=eyJpdiI6ImM2TGhYWmNvQ3VDUGRpR0h2bVNHQUE9PSIsInZhbHVlIjoic0VocmgyQ1FcL3JXR29La3lHOEFVUWc9PSIsIm1hYyI6IjMwZjI4MjM1MWE2Nzg0ODllYjA5ZDExMGExNGEzZjUxODM3NjczZGQ3OTVmYjU1MTY5NjIzNjhhZWY0YTBhNjYifQ%3D%3D; Hm_lvt_37b39b5356e9556531e38d50ddd8c555=1668769217,1669454806,1669625334,1669865201; tz=Etc/GMT-8 %2B08%3A00; _gid=GA1.3.131516366.1671088401; _ga=GA1.1.654970337.1664270832; _hjIncludedInSessionSample=0; _hjSession_915836=eyJpZCI6IjhmMjRkZjFjLTIxNzItNDJiNi1iMzliLWJiNWJlNWU2MGI0MyIsImNyZWF0ZWQiOjE2NzEyNTcxMTYyMzUsImluU2FtcGxlIjpmYWxzZX0=; crisp-client%2Fsession%2Fa8acb4a0-a13f-4d09-b433-ea92cabf4252=session_3f0b6dba-d64e-4769-a5db-bb7088193152; token=70d9594c8b7ece4146dbc8514791b204; selector=a42070e3c4ae291da26a41f89fba3750; snov_io=dLjJqLl2P4u2y1rb8EaknE4BaoiZnL5CUYwswgVH; st_ua=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NzEyODU5MjQsImRhdGEiOnsidXNlciI6eyJpZCI6MTg4MjA0NCwiZW1haWwiOiJodWFqaWFubW9iaWxlQGdtYWlsLmNvbSIsIm5hbWUiOiJKaWFuIEppYW4iLCJjb3VudHJ5IjoiQ04iLCJsYW5nIjoiemgiLCJzZXNzaW9uU3RhcnRlZEF0TXMiOjE2NzEyNTcxMjQ0NjksImN1cnJlbmN5SWQiOjEsInRpbWV6b25lIjoiQXNpYVwvU2hhbmdoYWkiLCJ0ZWFtIjp7ImlzTGVhZCI6MH19fX0.kFwo9JK4P4V64PZD_K2Y2ETPtU9WspIG7_KNKgVmSJQ; Hm_lpvt_37b39b5356e9556531e38d50ddd8c555=1671257125; _ga_BNRTCNFP5Y=GS1.1.1671257115.83.1.1671257142.33.0.0; XSRF-TOKEN=eyJpdiI6InY1NjhnQjFjb2puZTVDaWRcLytRU21RPT0iLCJ2YWx1ZSI6IlwvUm5IMEZ6UTAxK3R4Q3JvXC9DODBDQ3pWc1dPVXBHNDE1eTNqNEdNZzUxY2lPUTFGcmdNcFBGeFNQdGZGYktCRTNWWFwvQldnY01idHZDYVlBVDJ6aVNnPT0iLCJtYWMiOiI5MzQzYWI2ODAzOGUxMGViZDVjMDQwODk3ZjI1OThkNzJkYmQ2NmUyZWM5NmVhNGJhODgxZjg2MGU1OTQzYThmIn0%3D',
    'DNT': '1',
    'Origin': 'https://app.snov.io',
    'Pragma': 'no-cache',
    'Referer': 'https://app.snov.io/database-search',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'X-CSRF-Token': 'F0QX9Pgwe9ZCtAY4ymnfufe8Ze2NrG5j9wylj4D9',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'eyJpdiI6InY1NjhnQjFjb2puZTVDaWRcLytRU21RPT0iLCJ2YWx1ZSI6IlwvUm5IMEZ6UTAxK3R4Q3JvXC9DODBDQ3pWc1dPVXBHNDE1eTNqNEdNZzUxY2lPUTFGcmdNcFBGeFNQdGZGYktCRTNWWFwvQldnY01idHZDYVlBVDJ6aVNnPT0iLCJtYWMiOiI5MzQzYWI2ODAzOGUxMGViZDVjMDQwODk3ZjI1OThkNzJkYmQ2NmUyZWM5NmVhNGJhODgxZjg2MGU1OTQzYThmIn0=',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'filters': {
        'company': {
            'locations': {
                'include': [
                    {
                        'id': 41,
                        'locality': 'Canada',
                        'locationType': 'country',
                    },
                ],
                'exclude': [],
            },
            'industries': {
                'include': [
                    {
                        'id': 87,
                        'name': 'Medical Device',
                    },
                ],
                'exclude': [],
            },
            'size': {
                'id': 3,
                'code': 'C',
                'size': '11-50',
            },
        },
    },
}
    country_data = {
        "United States":236,
        "United Kingdom":235,
        "Germany":83,
        "Canada":41,
        "Luxembourg":130,
        "Ireland":107,
        "Switzerland":216,
        "Norway":166,
        "Iceland":102,
        "Denmark":61,
        "Sweden":215,
        "Netherlands":157,
        "Finland":75,
        "Austria":15,
        "Belgium":22,
        "San Marino":193,
        "France":76,
        "Andorra":6,
        "Italy":110,
        "Malta":138,
        "Spain":209,
        "Slovenia":203,
        "Estonia":70,
        "Cyprus":59,

    }
    industries_data = {
        # "Machinery":80,
        # "Measuring and Control Instrument Manufacturing":237,
        # "Metal Valve, Ball, and Roller Manufacturing":229,
        # "Metalworking Machinery Manufacturing":233,
        # "Railroad Manufacture":118,
        # "Communications Equipment Manufacturing":235,
        # "Industrial Automation":62,
        # "Mechanical Or Industrial Engineering":85,
    }
    def __init__(self,locality,industries) -> None:
        self.set_industries_data()
        self.set_industries(industries=industries)
        self.set_locality(locality =locality)
        url = "http://192.168.1.10:8000/snov/get_cookies"
        cookies = requests.get(url)
        cookies  = json.loads(cookies.text)
        self.cookies.update(cookies)

        url  = "http://192.168.1.10:8000/snov/get_header"
        headers =  json.loads(requests.get(url).text)
        self.headers.update(headers)
        self.headers["Referer"] =  'https://app.snov.io/database-search'


    def set_industries_data(self):
        par  = params()
        companyIndustries  = par.read_localjson("data.json")['companyIndustries']
        for i in companyIndustries:
            id = i["id"]

            name = i["name"]
            self.industries_data[name] = id
        
    
    def set_locality(self,locality):
        self.json_data["filters"]["company"]["locations"]["include"][0]["locality"] = locality
        self.json_data["filters"]["company"]["locations"]["include"][0]["id"] = self.country_data[locality]
         


    def set_industries(self,industries):
        self.json_data["filters"]["company"]["industries"]["include"][0]["name"] = industries
        try:
            industries =self.industries_data[industries]
        except:
            industries = ""
        self.json_data["filters"]["company"]["industries"]["include"][0]["id"] = industries


    def get_task_id(self):
        self.set_industries_data()
        response = trypost('https://app.snov.io/new/company-profile-search/search', cookies=self.cookies, headers=self.headers, json=self.json_data)
        return response.json()


if __name__ == "__main__":
    locality = "Cyprus"
    indus = "Shipbuilding"
    task =  Task(locality=locality,industries=indus)
    id = task.get_task_id()['data']['taskId']
    a = 1
    
    # task.set_industries_data()





