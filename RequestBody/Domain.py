#获取输入公司的域名信息

#根据api调用
from BaseRequestBody import *
import requests
from utils.TryRequest import *
class DomainCompanies(BaseRequestBody):
    cookies = {
        '_gcl_au': '1.1.32341399.1672211150',
        '_ga': 'GA1.3.290382776.1672211150',
        '_ga': 'GA1.1.290382776.1672211150',
        'tz': 'Etc/GMT-8 %2B08%3A00',
        'snovTrackingId': 'EUaxfzTRPXMxdwGbYymyX5mctnO9VqNzWqUfXNWFxTulZvst32Aw9oN9zHdRQdCi',
        'snovTrackingId': 'EUaxfzTRPXMxdwGbYymyX5mctnO9VqNzWqUfXNWFxTulZvst32Aw9oN9zHdRQdCi',
        'userId': '04344882792afc5e98425d82bb6895e7932c616539bd3fd1fd455c4082bc7858',
        '_hjSessionUser_915836': 'eyJpZCI6IjdjZDMzN2NlLWVkMDYtNWNlNS05YjBkLTNhNDJiNDMzNDNmYiIsImNyZWF0ZWQiOjE2NzIyMTExNjAyMzgsImV4aXN0aW5nIjp0cnVlfQ==',
        'Hm_lvt_37b39b5356e9556531e38d50ddd8c555': '1669865201',
        '_gid': 'GA1.3.1302700768.1672301190',
        'crisp-client%2Fsession%2Fa8acb4a0-a13f-4d09-b433-ea92cabf4252': 'session_4b8c5b18-d0cf-4943-918c-c016c79a90c7',
        'token': 'a6b9a418c4e92272cf5b1b80abd328cc',
        'selector': '593533f34e9f3584c5f5180fcce59489',
        'snov_io': '2s0yC4tiJPRmk14yBEjAGCgpW980eOCf0tuSgWaW',
        'st_ua': 'eyJ0eXAiOiJKV1QiLCasd13ssJ9.eyJleHAiOjE2NzIzMjk5OTMsImRhdGEiOnsidXNlciI6eyJpZCI6MTg4MjA0NCwiZW1haWwiOiJodWFqaWFubW9iaWxlQGdtYWlsLmNvbSIsIm5hbWUiOiJKaWFuIEppYW4iLCJjb3VudHJ5IjoiQ04iLCJsYW5nIjoiemgiLCJzZXNzaW9uU3RhcnRlZEF0TXMiOjE2NzIzMDExOTMxNzgsImN1cnJlbmN5SWQiOjEsInRpbWV6b25lIjoiQXNpYVwvU2hhbmdoYWkiLCJ0ZWFtIjp7ImlzTGVhZCI6MH19fX0.lezvXEis4YV789o3GddkeD-77MvsRqwYpIJHqcDQ_6k',
        'lang': 'eyJpdiI6IjZhK2ZCZnVtUWJqdGZ1VkFxSmJvc2c9PSIsInZhbHVlIjoiMkRGTmFXMHI1NVBqK05pdXFxUGw5QT09IiwibWFjIjoiYTE1NjU5OGU1OTAwOTU0NmQwZGQyYjE1MjkxMGQ1ZjM2MDZkZjQzZGE0NzNmZGU0M2JjMWFhMWE1MmY5OGUyYyJ9',
        'Hm_lpvt_37b39b5356e9556531e38d50ddd8c555': '1672301195',
        '_gat_UA-94112226-2': '1',
        '_gat_UA-94112226-3': '1',
        '_ga_BNRTCNFP5Y': 'GS1.1.1672304009.5.0.1672304009.60.0.0',
        '_hjIncludedInSessionSample': '0',
        '_hjSession_915836': 'eyJpZCI6ImE2MDQyZDI0LTlmYmUtNDg2NS05ZmFiLWFkZWI1MmIzNGM2YSIsImNyZWF0ZWQiOjE2NzIzMDQwMDk3ODMsImluU2FtcGxlIjpmYWxzZX0=',
        'XSRF-TOKEN': 'asdasdasdqws1sa3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ja;q=0.6,et;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': '_gcl_au=1.1.32341399.1672211150; _ga=GA1.3.290382776.1672211150; _ga=GA1.1.290382776.1672211150; tz=Etc/GMT-8 %2B08%3A00; snovTrackingId=EUaxfzTRPXMxdwGbYymyX5mctnO9VqNzWqUfXNWFxTulZvst32Aw9oN9zHdRQdCi; snovTrackingId=EUaxfzTRPXMxdwGbYymyX5mctnO9VqNzWqUfXNWFxTulZvst32Aw9oN9zHdRQdCi; userId=04344882792afc5e98425d82bb6895e7932c616539bd3fd1fd455c4082bc7858; _hjSessionUser_915836=eyJpZCI6IjdjZDMzN2NlLWVkMDYtNWNlNS05YjBkLTNhNDJiNDMzNDNmYiIsImNyZWF0ZWQiOjE2NzIyMTExNjAyMzgsImV4aXN0aW5nIjp0cnVlfQ==; Hm_lvt_37b39b5356e9556531e38d50ddd8c555=1669865201; _gid=GA1.3.1302700768.1672301190; crisp-client%2Fsession%2Fa8acb4a0-a13f-4d09-b433-ea92cabf4252=session_4b8c5b18-d0cf-4943-918c-c016c79a90c7; token=a6b9a418c4e92272cf5b1b80abd328cc; selector=593533f34e9f3584c5f5180fcce59489; snov_io=2s0yC4tiJPRmk14yBEjAGCgpW980eOCf0tuSgWaW; st_ua=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NzIzMjk5OTMsImRhdGEiOnsidXNlciI6eyJpZCI6MTg4MjA0NCwiZW1haWwiOiJodWFqaWFubW9iaWxlQGdtYWlsLmNvbSIsIm5hbWUiOiJKaWFuIEppYW4iLCJjb3VudHJ5IjoiQ04iLCJsYW5nIjoiemgiLCJzZXNzaW9uU3RhcnRlZEF0TXMiOjE2NzIzMDExOTMxNzgsImN1cnJlbmN5SWQiOjEsInRpbWV6b25lIjoiQXNpYVwvU2hhbmdoYWkiLCJ0ZWFtIjp7ImlzTGVhZCI6MH19fX0.lezvXEis4YV789o3GddkeD-77MvsRqwYpIJHqcDQ_6k; lang=eyJpdiI6IjZhK2ZCZnVtUWJqdGZ1VkFxSmJvc2c9PSIsInZhbHVlIjoiMkRGTmFXMHI1NVBqK05pdXFxUGw5QT09IiwibWFjIjoiYTE1NjU5OGU1OTAwOTU0NmQwZGQyYjE1MjkxMGQ1ZjM2MDZkZjQzZGE0NzNmZGU0M2JjMWFhMWE1MmY5OGUyYyJ9; Hm_lpvt_37b39b5356e9556531e38d50ddd8c555=1672301195; _gat_UA-94112226-2=1; _gat_UA-94112226-3=1; _ga_BNRTCNFP5Y=GS1.1.1672304009.5.0.1672304009.60.0.0; _hjIncludedInSessionSample=0; _hjSession_915836=eyJpZCI6ImE2MDQyZDI0LTlmYmUtNDg2NS05ZmFiLWFkZWI1MmIzNGM2YSIsImNyZWF0ZWQiOjE2NzIzMDQwMDk3ODMsImluU2FtcGxlIjpmYWxzZX0=; XSRF-TOKEN=eyJpdiI6IkNuOTJ5ZjdESTdBcUxZZ0VCM2tnUXc9PSIsInZhbHVlIjoiNmV4TzQ2OFNyOXVsU3l4VmgrSDJNTk05cjhKcVpmYmU3ZndpdUc2Ynd5YVwva3VvZFwvRDR3M0hQVFJVZUVzK29cL2tiWVRVUVdHQ3kzT2RvOW91bmNaa0E9PSIsIm1hYyI6IjczNjdkZjkxOTk5MDY0OTI4YWMyMGZmOThkMGE3NTU3Y2Q3OTc1MjI0NWVjZTVjZDMyOTA2MzU5Y2MyODZiMjAifQ%3D%3D',
        'DNT': '1',
        'Origin': 'https://app.snov.io',
        'Pragma': 'no-cache',
        'Referer': 'https://app.snov.io/database-search',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'X-CSRF-Token': 'aasdasd',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6asdasdasdwasqweTdBcUxZZ0VCM2tnUXc9PSIsInZhbHVlIjoiNmV4TzQ2OFNyOXVsU3l4VmgrSDJNTk05cjhKcVpmYmU3ZndpdUc2Ynd5YVwva3VvZFwvRDR3M0hQVFJVZUVzK29cL2tiWVRVUVdHQ3kzT2RvOW91bmNaa0E9PSIsIm1hYyI6IjczNjdkZjkxOTk5MDY0OTI4YWMyMGZmOThkMGE3NTU3Y2Q3OTc1MjI0NWVjZTVjZDMyOTA2MzU5Y2MyODZiMjAifQ==',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'query': 'ddd',
    }
    def get_domain_companies(self,query):
        self.json_data['query'] = query
        response = trypost('https://app.snov.io/search/domainCompanies', cookies=self.cookies, headers=self.headers, json=self.json_data)
        return response
  

if __name__ == "__main__":
    domaincompanies = DomainCompanies()
    res = domaincompanies.get_domain_companies("ddd").json()
    a = 1
