import requests
import time
import json
from RequestBody.SnovBaseRequestBody import SnovBaseRequestBody
from RequestBody.utils.TryRequest import *
class SnovEmaillist(SnovBaseRequestBody):
    cookies = {
    'snovTrackingId': 'jzrUnINGUvpXtOGwPzoG8sYo4yNzlyUM50U6q9zbWnlDybqW0KfZccc270BVZJEB',
    '_ga': 'GA1.3.654970337.1664270832',
    'snovTrackingId': 'jzrUnINGUvpXtOGwPzoG8sYo4yNzlyUM50U6q9zbWnlDybqW0KfZccc270BVZJEB',
    '_hjSessionUser_915836': 'eyJpZCI6Ijc0MzdkMzdiLTZmOGYtNTg1YS1hNzAxLTViN2VkOTRmYTEzYiIsImNyZWF0ZWQiOjE2NjQyNzA4MzI1NDgsImV4aXN0aW5nIjp0cnVlfQ==',
    'psuid': 'e2e845b3-8efc-4cd4-8a91-2afe3d5f325d',
    'userId': '04344882792afc5e98425d82bb6895e7932c616539bd3fd1fd455c4082bc7858',
    'lang': 'eyJpdiI6ImM2TGhYWmNvQ3VDUGRpR0h2bVNHQUE9PSIsInZhbHVlIjoic0VocmgyQ1FcL3JXR29La3lHOEFVUWc9PSIsIm1hYyI6IjMwZjI4MjM1MWE2Nzg0ODllYjA5ZDExMGExNGEzZjUxODM3NjczZGQ3OTVmYjU1MTY5NjIzNjhhZWY0YTBhNjYifQ%3D%3D',
    'tz': 'Etc/GMT-8 %2B08%3A00',
    'selector': '60bf055a51c7d25d56e985149a8639eb',
    'Hm_lvt_37b39b5356e9556531e38d50ddd8c555': '1669625334,1669865201',
    '_gcl_au': '1.1.696473263.1672109182',
    '_gid': 'GA1.3.1071694354.1672109182',
    '_hjSession_915836': 'eyJpZCI6ImVmM2M1MmVkLTFiN2YtNDZiNC1iMDQ5LWQ2MzJmZWIwMjU3MyIsImNyZWF0ZWQiOjE2NzIxMDkxODMwNDEsImluU2FtcGxlIjpmYWxzZX0=',
    'token': 'f8f16ad8df44bb1b1c7d09a4b4aea63b',
    'snov_io': 'MRljlzkZfV0Q3Pdik2875SRZF7thS9nKcfwNNRyb',
    'crisp-client%2Fsession%2Fa8acb4a0-a13f-4d09-b433-ea92cabf4252': 'session_1cd344aa-4fdf-4574-ac6f-56dd574e05a8',
    'st_ua': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NzIxMzc5ODUsImRhdGEiOnsidXNlciI6eyJpZCI6MTg4MjA0NCwiZW1haWwiOiJodWFqaWFubW9iaWxlQGdtYWlsLmNvbSIsIm5hbWUiOiJKaWFuIEppYW4iLCJjb3VudHJ5IjoiQ04iLCJsYW5nIjoiemgiLCJzZXNzaW9uU3RhcnRlZEF0TXMiOjE2NzIxMDkxODUwODEsImN1cnJlbmN5SWQiOjEsInRpbWV6b25lIjoiQXNpYVwvU2hhbmdoYWkiLCJ0ZWFtIjp7ImlzTGVhZCI6MH19fX0.0-y6b5AtKEkDFw7P1zpi6sL8nBvrJI9xevfTzw9H3F0',
    'Hm_lpvt_37b39b5356e9556531e38d50ddd8c555': '1672109192',
    '_gid': 'GA1.2.1071694354.1672109182',
    '_ga': 'GA1.1.654970337.1664270832',
    'crisp-client%2Fsocket%2Fa8acb4a0-a13f-4d09-b433-ea92cabf4252': '0',
    '_ga_BNRTCNFP5Y': 'GS1.1.1672109182.89.1.1672110289.23.0.0',
    'XSRF-TOKEN': 'eyJpdiI6ImtaMnM4aVp5ZVczV2FLeXNRN1o1dEE9PSIsInZhbHVlIjoiOVVjNThDNEpjckNrM3JNdmFWdXVNODNXckdQelh1TjJsQUNERUg0SW0wQUwwaGdvTXdyZWxyaEw0Q2FIQmNvUlNlZVhDVndVMWF5RllZZEIwUE5ORlE9PSIsIm1hYyI6ImU0NmY0MTRmMDE3OGY4ODlhYTg3NjczMWMxMTRkYmMzN2RmNzM0NmY2Mzg2ZGNlYTZlZTc5YjcyZmYzMWMzYjEifQ%3D%3D',
}

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ja;q=0.6,et;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'snovTrackingId=jzrUnINGUvpXtOGwPzoG8sYo4yNzlyUM50U6q9zbWnlDybqW0KfZccc270BVZJEB; _ga=GA1.3.654970337.1664270832; snovTrackingId=jzrUnINGUvpXtOGwPzoG8sYo4yNzlyUM50U6q9zbWnlDybqW0KfZccc270BVZJEB; _hjSessionUser_915836=eyJpZCI6Ijc0MzdkMzdiLTZmOGYtNTg1YS1hNzAxLTViN2VkOTRmYTEzYiIsImNyZWF0ZWQiOjE2NjQyNzA4MzI1NDgsImV4aXN0aW5nIjp0cnVlfQ==; psuid=e2e845b3-8efc-4cd4-8a91-2afe3d5f325d; userId=04344882792afc5e98425d82bb6895e7932c616539bd3fd1fd455c4082bc7858; lang=eyJpdiI6ImM2TGhYWmNvQ3VDUGRpR0h2bVNHQUE9PSIsInZhbHVlIjoic0VocmgyQ1FcL3JXR29La3lHOEFVUWc9PSIsIm1hYyI6IjMwZjI4MjM1MWE2Nzg0ODllYjA5ZDExMGExNGEzZjUxODM3NjczZGQ3OTVmYjU1MTY5NjIzNjhhZWY0YTBhNjYifQ%3D%3D; tz=Etc/GMT-8 %2B08%3A00; selector=60bf055a51c7d25d56e985149a8639eb; Hm_lvt_37b39b5356e9556531e38d50ddd8c555=1669625334,1669865201; _gcl_au=1.1.696473263.1672109182; _gid=GA1.3.1071694354.1672109182; _hjSession_915836=eyJpZCI6ImVmM2M1MmVkLTFiN2YtNDZiNC1iMDQ5LWQ2MzJmZWIwMjU3MyIsImNyZWF0ZWQiOjE2NzIxMDkxODMwNDEsImluU2FtcGxlIjpmYWxzZX0=; token=f8f16ad8df44bb1b1c7d09a4b4aea63b; snov_io=MRljlzkZfV0Q3Pdik2875SRZF7thS9nKcfwNNRyb; crisp-client%2Fsession%2Fa8acb4a0-a13f-4d09-b433-ea92cabf4252=session_1cd344aa-4fdf-4574-ac6f-56dd574e05a8; st_ua=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NzIxMzc5ODUsImRhdGEiOnsidXNlciI6eyJpZCI6MTg4MjA0NCwiZW1haWwiOiJodWFqaWFubW9iaWxlQGdtYWlsLmNvbSIsIm5hbWUiOiJKaWFuIEppYW4iLCJjb3VudHJ5IjoiQ04iLCJsYW5nIjoiemgiLCJzZXNzaW9uU3RhcnRlZEF0TXMiOjE2NzIxMDkxODUwODEsImN1cnJlbmN5SWQiOjEsInRpbWV6b25lIjoiQXNpYVwvU2hhbmdoYWkiLCJ0ZWFtIjp7ImlzTGVhZCI6MH19fX0.0-y6b5AtKEkDFw7P1zpi6sL8nBvrJI9xevfTzw9H3F0; Hm_lpvt_37b39b5356e9556531e38d50ddd8c555=1672109192; _gid=GA1.2.1071694354.1672109182; _ga=GA1.1.654970337.1664270832; crisp-client%2Fsocket%2Fa8acb4a0-a13f-4d09-b433-ea92cabf4252=0; _ga_BNRTCNFP5Y=GS1.1.1672109182.89.1.1672110289.23.0.0; XSRF-TOKEN=eyJpdiI6ImtaMnM4aVp5ZVczV2FLeXNRN1o1dEE9PSIsInZhbHVlIjoiOVVjNThDNEpjckNrM3JNdmFWdXVNODNXckdQelh1TjJsQUNERUg0SW0wQUwwaGdvTXdyZWxyaEw0Q2FIQmNvUlNlZVhDVndVMWF5RllZZEIwUE5ORlE9PSIsIm1hYyI6ImU0NmY0MTRmMDE3OGY4ODlhYTg3NjczMWMxMTRkYmMzN2RmNzM0NmY2Mzg2ZGNlYTZlZTc5YjcyZmYzMWMzYjEifQ%3D%3D',
        'DNT': '1',
        'Origin': 'https://app.snov.io',
        'Pragma': 'no-cache',
        'Referer': 'https://app.snov.io/companies',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'X-CSRF-Token': 'ck05chbTo5sKZQCMUt1uC5Ytlo44qiLEfRL87hJf',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6ImtaMnM4aVp5ZVczV2FLeXNRN1o1dEE9PSIsInZhbHVlIjoiOVVjNThDNEpjckNrM3JNdmFWdXVNODNXckdQelh1TjJsQUNERUg0SW0wQUwwaGdvTXdyZWxyaEw0Q2FIQmNvUlNlZVhDVndVMWF5RllZZEIwUE5ORlE9PSIsIm1hYyI6ImU0NmY0MTRmMDE3OGY4ODlhYTg3NjczMWMxMTRkYmMzN2RmNzM0NmY2Mzg2ZGNlYTZlZTc5YjcyZmYzMWMzYjEifQ==',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'isGreen': True,
        'lastId': 0,
        'perPage': 20,
        'page': 1,
    }
    def set_page(self,page):
        self.json_data["page"] = page 

    def set_lastId(self,lastId):
        self.json_data['lastId'] = lastId

    def getemail(self,company_id,page=None): #等待修改为获得所有邮箱
        url = 'https://app.snov.io/companies/e7d1386feda53463e1ead8906f7d8c6f46797ed30940ee6804692f8b360a3897563856/emails'.replace('e7d1386feda53463e1ead8906f7d8c6f46797ed30940ee6804692f8b360a3897563856',company_id)
        
        response = trypost(url, cookies=self.cookies, headers=self.headers, json=self.json_data).json()
        emailsTotal = response['data']['emailsTotal']
        emailList = response['data']['list']
        lastId =  response['data']['lastId']
        page_count  = emailsTotal
        startpage = 1
        endpage = int((page_count/50)+0.99)
        # while 
        return emailList
            #     if response.status_code==200:
            #         return json.loads(response.text)['data']['list']
            #     else:
            #         print('太多请求 休息一会zzz')
            #         time.sleep(2)
                    
            # except:
            #     print('抓邮件被发现了 休息一会zzz')
            #     time.sleep(2)


if __name__ =="__main__":
    email = SnovEmaillist()
    res = email.getemail('e7d1386feda53463e1ead8906f7d8c6f46797ed30940ee6804692f8b360a3897563856')
    a = 1          

        