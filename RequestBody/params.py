import requests
import json
import sys
from SnovBaseRequestBody import *

class params(SnovBaseRequestBody):
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
        'selector': 'f08c0c4a5cc077ed4bc4370659e0baaf',
        'Hm_lpvt_37b39b5356e9556531e38d50ddd8c555': '1671001174',
        'snov_io': 'jAl2f8YFI20fWe4z5pbtmO7f4daBeBXz2kTFlC7e',
        'st_ua': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NzExMTcxOTksImRhdGEiOnsidXNlciI6eyJpZCI6MTg4MjA0NCwiZW1haWwiOiJodWFqaWFubW9iaWxlQGdtYWlsLmNvbSIsIm5hbWUiOiJKaWFuIEppYW4iLCJjb3VudHJ5IjoiQ04iLCJsYW5nIjoiemgiLCJzZXNzaW9uU3RhcnRlZEF0TXMiOjE2NzEwODgzOTk0MTgsImN1cnJlbmN5SWQiOjEsInRpbWV6b25lIjoiQXNpYVwvU2hhbmdoYWkiLCJ0ZWFtIjp7ImlzTGVhZCI6MH19fX0.uFj7gjzxoCgTnKPpbmqHgQa0FwDKtj1jnK43CJ2CVNA',
        '_gid': 'GA1.3.131516366.1671088401',
        'crisp-client%2Fsession%2Fa8acb4a0-a13f-4d09-b433-ea92cabf4252': 'session_b97fe0a7-6698-4924-8e46-6edb941a24a9',
        '_hjIncludedInSessionSample': '0',
        '_hjSession_915836': 'eyJpZCI6IjU0ZDIxNDEwLTg3ZTQtNGMyYi04NmFlLTg0YjU3MjdlYjZhYiIsImNyZWF0ZWQiOjE2NzEwOTU0NjQzOTYsImluU2FtcGxlIjpmYWxzZX0=',
        '_gid': 'GA1.2.131516366.1671088401',
        'token': '3568fec31606227e510439b8107f86ad',
        '_ga': 'GA1.1.654970337.1664270832',
        '_gat_UA-94112226-2': '1',
        '_gat_UA-94112226-3': '1',
        'XSRF-TOKEN': 'eyJpdiI6IlF6TVo1TWNCVkdYUDk1WHA1UGZ5blE9PSIsInZhbHVlIjoidWRtdXVMaTljbjJYWUtzSUdjYUd6Q2FGVVU2MmVhXC9UR0dIaWdHYWNtOVpJbFRUXC9DWU50T3k1ektKREh4KzJhS1Q3TDhPQU5hQTlIZ1VwZ0lHUFkrdz09IiwibWFjIjoiMDMwN2FkZTBlNDA0OTVmNTg1OWVjZmQzMzU3ZTljZTdmMGVhNmVkZWQxZTM2MmMzMmQ2MmUxNWMyNDk1MjA4MyJ9',
        '_ga_BNRTCNFP5Y': 'GS1.1.1671098161.75.1.1671098200.21.0.0',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ja;q=0.6,et;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'snovTrackingId=jzrUnINGUvpXtOGwPzoG8sYo4yNzlyUM50U6q9zbWnlDybqW0KfZccc270BVZJEB; _gcl_au=1.1.1271293594.1664270831; _ga=GA1.3.654970337.1664270832; snovTrackingId=jzrUnINGUvpXtOGwPzoG8sYo4yNzlyUM50U6q9zbWnlDybqW0KfZccc270BVZJEB; _hjSessionUser_915836=eyJpZCI6Ijc0MzdkMzdiLTZmOGYtNTg1YS1hNzAxLTViN2VkOTRmYTEzYiIsImNyZWF0ZWQiOjE2NjQyNzA4MzI1NDgsImV4aXN0aW5nIjp0cnVlfQ==; psuid=e2e845b3-8efc-4cd4-8a91-2afe3d5f325d; userId=04344882792afc5e98425d82bb6895e7932c616539bd3fd1fd455c4082bc7858; lang=eyJpdiI6ImM2TGhYWmNvQ3VDUGRpR0h2bVNHQUE9PSIsInZhbHVlIjoic0VocmgyQ1FcL3JXR29La3lHOEFVUWc9PSIsIm1hYyI6IjMwZjI4MjM1MWE2Nzg0ODllYjA5ZDExMGExNGEzZjUxODM3NjczZGQ3OTVmYjU1MTY5NjIzNjhhZWY0YTBhNjYifQ%3D%3D; Hm_lvt_37b39b5356e9556531e38d50ddd8c555=1668769217,1669454806,1669625334,1669865201; tz=Etc/GMT-8 %2B08%3A00; selector=f08c0c4a5cc077ed4bc4370659e0baaf; Hm_lpvt_37b39b5356e9556531e38d50ddd8c555=1671001174; snov_io=jAl2f8YFI20fWe4z5pbtmO7f4daBeBXz2kTFlC7e; st_ua=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NzExMTcxOTksImRhdGEiOnsidXNlciI6eyJpZCI6MTg4MjA0NCwiZW1haWwiOiJodWFqaWFubW9iaWxlQGdtYWlsLmNvbSIsIm5hbWUiOiJKaWFuIEppYW4iLCJjb3VudHJ5IjoiQ04iLCJsYW5nIjoiemgiLCJzZXNzaW9uU3RhcnRlZEF0TXMiOjE2NzEwODgzOTk0MTgsImN1cnJlbmN5SWQiOjEsInRpbWV6b25lIjoiQXNpYVwvU2hhbmdoYWkiLCJ0ZWFtIjp7ImlzTGVhZCI6MH19fX0.uFj7gjzxoCgTnKPpbmqHgQa0FwDKtj1jnK43CJ2CVNA; _gid=GA1.3.131516366.1671088401; crisp-client%2Fsession%2Fa8acb4a0-a13f-4d09-b433-ea92cabf4252=session_b97fe0a7-6698-4924-8e46-6edb941a24a9; _hjIncludedInSessionSample=0; _hjSession_915836=eyJpZCI6IjU0ZDIxNDEwLTg3ZTQtNGMyYi04NmFlLTg0YjU3MjdlYjZhYiIsImNyZWF0ZWQiOjE2NzEwOTU0NjQzOTYsImluU2FtcGxlIjpmYWxzZX0=; _gid=GA1.2.131516366.1671088401; token=3568fec31606227e510439b8107f86ad; _ga=GA1.1.654970337.1664270832; _gat_UA-94112226-2=1; _gat_UA-94112226-3=1; XSRF-TOKEN=eyJpdiI6IlF6TVo1TWNCVkdYUDk1WHA1UGZ5blE9PSIsInZhbHVlIjoidWRtdXVMaTljbjJYWUtzSUdjYUd6Q2FGVVU2MmVhXC9UR0dIaWdHYWNtOVpJbFRUXC9DWU50T3k1ektKREh4KzJhS1Q3TDhPQU5hQTlIZ1VwZ0lHUFkrdz09IiwibWFjIjoiMDMwN2FkZTBlNDA0OTVmNTg1OWVjZmQzMzU3ZTljZTdmMGVhNmVkZWQxZTM2MmMzMmQ2MmUxNWMyNDk1MjA4MyJ9; _ga_BNRTCNFP5Y=GS1.1.1671098161.75.1.1671098200.21.0.0',
        'DNT': '1',
        'Pragma': 'no-cache',
        'Referer': 'https://app.snov.io/database-search',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'X-CSRF-Token': 'Xw4x0kBwwP3KeT0dsW73YCZvku55dOKNPOWvP3jr',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6IlF6TVo1TWNCVkdYUDk1WHA1UGZ5blE9PSIsInZhbHVlIjoidWRtdXVMaTljbjJYWUtzSUdjYUd6Q2FGVVU2MmVhXC9UR0dIaWdHYWNtOVpJbFRUXC9DWU50T3k1ektKREh4KzJhS1Q3TDhPQU5hQTlIZ1VwZ0lHUFkrdz09IiwibWFjIjoiMDMwN2FkZTBlNDA0OTVmNTg1OWVjZmQzMzU3ZTljZTdmMGVhNmVkZWQxZTM2MmMzMmQ2MmUxNWMyNDk1MjA4MyJ9',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    def getparams(self):
        response = requests.get('https://app.snov.io/new/company-profile-search/params', cookies=self.cookies, headers=self.headers)
        import json
        response = json.loads(response.text)
        self.response = response
        return response

    def write_local(self):
        json_data = self.response["data"]
        b = json.dumps(json_data)
        f2 = open('data.json', 'w')
        f2.write(b)
        f2.close()
    

    def read_localjson(self,filename):
        f = open(filename, 'r')
        content = f.read()
        content = json.loads(content)
        return content


if __name__ =="__main__":
    par = params()
    data = par.getparams()["data"]
    companyIndustries = data["companyIndustries"]
    companyRevenues = data["companyRevenues"]
    companySizeCodes = data["companySizeCodes"]
    par.write_local()
    data  = par.read_localjson("data.json")
    a =1 
    

    



