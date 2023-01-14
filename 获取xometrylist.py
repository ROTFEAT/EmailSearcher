import requests

cookies = {
    '_gcl_au': '1.1.633934323.1673402517',
    'ajs_anonymous_id': '50078fd2-647b-4f4f-a443-ff3403874e2e',
    'rj2session': '316bbba9-1a2a-4814-a202-0045c0b4bb5d',
    'utag_main': 'v_id:01859e900c9b00361a05039da7cc0506f001806700bd0$_sn:1$_se:1$_ss:1$_st:1673404318683$ses_id:1673402518683%3Bexp-session$_pn:1%3Bexp-session$dc_visit:1$dc_event:1%3Bexp-session$dc_region:us-west-2%3Bexp-session',
    'ajs_user_id': '6A056',
    '_gid': 'GA1.2.1814661586.1673402521',
    'mkjs_user_id': 'null',
    'mkjs_group_id': 'null',
    'drift_campaign_refresh': 'd05c549f-7074-4b35-b06c-c382cf758fd3',
    'QuantumMetricSessionID': '0534beac9052abf21036bad5e7518b27',
    'QuantumMetricUserID': 'b255f49e67f6dfa2d466352e5ed46c45',
    'access_token_cookie': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik16Z3lSalkyUWtGRVJEYzNNVGcwT0RkRlJUYzJNRVl5TlRkQlFVUkVRekEwTkRBME9FWXhSZyJ9.eyJodHRwczovL3d3dy54b21ldHJ5LmNvbS8iOnsidXNlcklkIjoiNkEwNTYiLCJlbWFpbEFkZHJlc3MiOiJodWFqaWFubW9iaWxlQGdtYWlsLmNvbSIsInN0YWZmUm9sZXMiOltdLCJuYW1lIjoiV0FORyBZWSIsImZlZGVyYXRlZElkZW50aXR5Ijp7ImFwcGxpY2F0aW9uVXNlcnMiOnsieG9tZXRyeSI6eyJ1c2VySWQiOiI2QTA1NiJ9LCJ0aG9tYXMiOnsidXNlcklkIjoiMjI4OTYxOTQ3In19fX0sImlzcyI6Imh0dHBzOi8vbG9naW4ueG9tZXRyeS5jb20vIiwic3ViIjoiYXV0aDB8NkEwNTYiLCJhdWQiOlsiaHR0cHM6Ly9zZXJ2aWNlcy54b21ldHJ5LmNvbSIsImh0dHBzOi8veG9tZXRyeS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjczNDAyNTMyLCJleHAiOjE2NzM0MTY5MzIsImF6cCI6ImZva2ZFOEZlTnpoMmRPM2FkRWlFemQxVngzOElRNVVhIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBvZmZsaW5lX2FjY2VzcyJ9.g4j_shox_CGxbA48hMcsLGNpUpPMt71g_ckzhsrAs4QBd150p445eB7959Y4ABIQhK88KkXmYcNS9z9Biky-go08eNt16jrrRVzHdpc5UId3NAx4Cw4BQj6TymhMPQqnGnrCInTXXYP4clWGF4vTsLhhQkQIpkPjvvDd-sQSTFtwUNH31y_IbD40nOafFI62AGM_YiKwB7b8230i0ld9Hi8o-Lemc9WFiqt0hul1yK-VTtneUTshMWpPLNQ3MKcn_Yp5WpzvY8D79zv886iXzO9C5D69vULTHRiFMi4h2nKT6xijenA8Pl-6w06mieSCVJLi3DJl858QT_bj29xvFg',
    'refresh_token_cookie': 'v1.MbTI6PeoIVKK9hUMbgvhQjycseV7CwysJ6aqyOeQ0HiOaNCCp138mjm9uj8yzneMOc52w9A44bDdWeah-SycfO0',
    'session': 'eyJhdXRoUGFyYW1zIjp7InNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUgb2ZmbGluZV9hY2Nlc3MiLCJub25jZSI6IjZiNDM1NDA0YjNjNmNiZjg4ZjcyYWIyMTIxMDhjYWZiIn0sInBhc3Nwb3J0Ijp7InVzZXIiOnsic3ViIjoiYXV0aDB8NkEwNTYiLCJuaWNrbmFtZSI6Imh1YWppYW5tb2JpbGUiLCJuYW1lIjoiV0FORyBZWSIsInBpY3R1cmUiOiJodHRwczovL3MuZ3JhdmF0YXIuY29tL2F2YXRhci9hZjE4NTZjZWU2OTIxZmJlMTdlZTUwMDk4YjRkNGY1OT9zPTQ4MCZyPXBnJmQ9aHR0cHMlM0ElMkYlMkZjZG4uYXV0aDAuY29tJTJGYXZhdGFycyUyRnd5LnBuZyIsInVwZGF0ZWRfYXQiOiIyMDIzLTAxLTExVDAyOjAyOjExLjUxNFoiLCJlbWFpbCI6Imh1YWppYW5tb2JpbGVAZ21haWwuY29tIiwiaHR0cHM6Ly93d3cueG9tZXRyeS5jb20vIjp7InVzZXJJZCI6IjZBMDU2IiwiZW1haWxBZGRyZXNzIjoiaHVhamlhbm1vYmlsZUBnbWFpbC5jb20iLCJzdGFmZlJvbGVzIjpbXSwibmFtZSI6IldBTkcgWVkiLCJmZWRlcmF0ZWRJZGVudGl0eSI6eyJhcHBsaWNhdGlvblVzZXJzIjp7InhvbWV0cnkiOnsidXNlcklkIjoiNkEwNTYifSwidGhvbWFzIjp7InVzZXJJZCI6IjIyODk2MTk0NyJ9fX19fX0sInJlZGlyZWN0VXJsIjoiaHR0cHM6Ly9nZXQueG9tZXRyeS5jb20ifQ==',
    'session.sig': 'sJ-FfUAvPXU2Jw9s9mpDiJrsarU',
    'ln_or': 'eyI5NDk1NiI6ImQifQ%3D%3D',
    'intercom-id-c31z56b8': 'ffd462ae-2c0a-43a4-b7eb-6232c13c196a',
    'intercom-device-id-c31z56b8': 'f333f938-870f-4dd7-9040-376224ff53c8',
    '__hstc': '70217615.c6eae9ec532377858a74bacfc96c9e1c.1673402544284.1673402544284.1673402544284.1',
    'hubspotutk': 'c6eae9ec532377858a74bacfc96c9e1c',
    '__hssrc': '1',
    '_ga': 'GA1.1.1924150895.1673402518',
    'analytics_session_id': '1673402521179',
    '_uetsid': 'ee217b00915311ed9a71ff9a352726a1',
    '_uetvid': '41a7beb059b411ed84b58d635a039a2e',
    '_ga_QMC4ND9KYZ': 'GS1.1.1673402517.1.1.1673403255.58.0.0',
    'intercom-session-c31z56b8': 'OUxpRFdMd1VjMys0UHF2cEdCOWM1Wjgyd0w0Lzlvck5DR0hVZDNZWVFrMmdMb0xNdmllKysxV0NmL1M3dFErOS0tOW5EYTgrMGtnd0hrSFpocDdjankzdz09--259a8b1c24f06508577aae0972a344ceac47c4f6',
    '__hssc': '70217615.5.1673402544285',
    '__cf_bm': 'Xwj5ZSAfEQ4UfFYUKjj_zn2gvmvVg_pu9qe5WbK0zak-1673403601-0-AXs0tm7JGy9hHMWD423dPHLvSE3sMuIi6aDqcgT8YlzS4+5Z5t8pdrlnEpzfRjiyrIJ2o6enoSGDduoKJ1gWhWw=',
}

headers = {
    'authority': 'www.xometry.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ja;q=0.6,et;q=0.5',
    'cache-control': 'no-cache',
    # 'cookie': '_gcl_au=1.1.633934323.1673402517; ajs_anonymous_id=50078fd2-647b-4f4f-a443-ff3403874e2e; rj2session=316bbba9-1a2a-4814-a202-0045c0b4bb5d; utag_main=v_id:01859e900c9b00361a05039da7cc0506f001806700bd0$_sn:1$_se:1$_ss:1$_st:1673404318683$ses_id:1673402518683%3Bexp-session$_pn:1%3Bexp-session$dc_visit:1$dc_event:1%3Bexp-session$dc_region:us-west-2%3Bexp-session; ajs_user_id=6A056; _gid=GA1.2.1814661586.1673402521; mkjs_user_id=null; mkjs_group_id=null; drift_campaign_refresh=d05c549f-7074-4b35-b06c-c382cf758fd3; QuantumMetricSessionID=0534beac9052abf21036bad5e7518b27; QuantumMetricUserID=b255f49e67f6dfa2d466352e5ed46c45; access_token_cookie=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik16Z3lSalkyUWtGRVJEYzNNVGcwT0RkRlJUYzJNRVl5TlRkQlFVUkVRekEwTkRBME9FWXhSZyJ9.eyJodHRwczovL3d3dy54b21ldHJ5LmNvbS8iOnsidXNlcklkIjoiNkEwNTYiLCJlbWFpbEFkZHJlc3MiOiJodWFqaWFubW9iaWxlQGdtYWlsLmNvbSIsInN0YWZmUm9sZXMiOltdLCJuYW1lIjoiV0FORyBZWSIsImZlZGVyYXRlZElkZW50aXR5Ijp7ImFwcGxpY2F0aW9uVXNlcnMiOnsieG9tZXRyeSI6eyJ1c2VySWQiOiI2QTA1NiJ9LCJ0aG9tYXMiOnsidXNlcklkIjoiMjI4OTYxOTQ3In19fX0sImlzcyI6Imh0dHBzOi8vbG9naW4ueG9tZXRyeS5jb20vIiwic3ViIjoiYXV0aDB8NkEwNTYiLCJhdWQiOlsiaHR0cHM6Ly9zZXJ2aWNlcy54b21ldHJ5LmNvbSIsImh0dHBzOi8veG9tZXRyeS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjczNDAyNTMyLCJleHAiOjE2NzM0MTY5MzIsImF6cCI6ImZva2ZFOEZlTnpoMmRPM2FkRWlFemQxVngzOElRNVVhIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBvZmZsaW5lX2FjY2VzcyJ9.g4j_shox_CGxbA48hMcsLGNpUpPMt71g_ckzhsrAs4QBd150p445eB7959Y4ABIQhK88KkXmYcNS9z9Biky-go08eNt16jrrRVzHdpc5UId3NAx4Cw4BQj6TymhMPQqnGnrCInTXXYP4clWGF4vTsLhhQkQIpkPjvvDd-sQSTFtwUNH31y_IbD40nOafFI62AGM_YiKwB7b8230i0ld9Hi8o-Lemc9WFiqt0hul1yK-VTtneUTshMWpPLNQ3MKcn_Yp5WpzvY8D79zv886iXzO9C5D69vULTHRiFMi4h2nKT6xijenA8Pl-6w06mieSCVJLi3DJl858QT_bj29xvFg; refresh_token_cookie=v1.MbTI6PeoIVKK9hUMbgvhQjycseV7CwysJ6aqyOeQ0HiOaNCCp138mjm9uj8yzneMOc52w9A44bDdWeah-SycfO0; session=eyJhdXRoUGFyYW1zIjp7InNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUgb2ZmbGluZV9hY2Nlc3MiLCJub25jZSI6IjZiNDM1NDA0YjNjNmNiZjg4ZjcyYWIyMTIxMDhjYWZiIn0sInBhc3Nwb3J0Ijp7InVzZXIiOnsic3ViIjoiYXV0aDB8NkEwNTYiLCJuaWNrbmFtZSI6Imh1YWppYW5tb2JpbGUiLCJuYW1lIjoiV0FORyBZWSIsInBpY3R1cmUiOiJodHRwczovL3MuZ3JhdmF0YXIuY29tL2F2YXRhci9hZjE4NTZjZWU2OTIxZmJlMTdlZTUwMDk4YjRkNGY1OT9zPTQ4MCZyPXBnJmQ9aHR0cHMlM0ElMkYlMkZjZG4uYXV0aDAuY29tJTJGYXZhdGFycyUyRnd5LnBuZyIsInVwZGF0ZWRfYXQiOiIyMDIzLTAxLTExVDAyOjAyOjExLjUxNFoiLCJlbWFpbCI6Imh1YWppYW5tb2JpbGVAZ21haWwuY29tIiwiaHR0cHM6Ly93d3cueG9tZXRyeS5jb20vIjp7InVzZXJJZCI6IjZBMDU2IiwiZW1haWxBZGRyZXNzIjoiaHVhamlhbm1vYmlsZUBnbWFpbC5jb20iLCJzdGFmZlJvbGVzIjpbXSwibmFtZSI6IldBTkcgWVkiLCJmZWRlcmF0ZWRJZGVudGl0eSI6eyJhcHBsaWNhdGlvblVzZXJzIjp7InhvbWV0cnkiOnsidXNlcklkIjoiNkEwNTYifSwidGhvbWFzIjp7InVzZXJJZCI6IjIyODk2MTk0NyJ9fX19fX0sInJlZGlyZWN0VXJsIjoiaHR0cHM6Ly9nZXQueG9tZXRyeS5jb20ifQ==; session.sig=sJ-FfUAvPXU2Jw9s9mpDiJrsarU; ln_or=eyI5NDk1NiI6ImQifQ%3D%3D; intercom-id-c31z56b8=ffd462ae-2c0a-43a4-b7eb-6232c13c196a; intercom-device-id-c31z56b8=f333f938-870f-4dd7-9040-376224ff53c8; __hstc=70217615.c6eae9ec532377858a74bacfc96c9e1c.1673402544284.1673402544284.1673402544284.1; hubspotutk=c6eae9ec532377858a74bacfc96c9e1c; __hssrc=1; _ga=GA1.1.1924150895.1673402518; analytics_session_id=1673402521179; _uetsid=ee217b00915311ed9a71ff9a352726a1; _uetvid=41a7beb059b411ed84b58d635a039a2e; _ga_QMC4ND9KYZ=GS1.1.1673402517.1.1.1673403255.58.0.0; intercom-session-c31z56b8=OUxpRFdMd1VjMys0UHF2cEdCOWM1Wjgyd0w0Lzlvck5DR0hVZDNZWVFrMmdMb0xNdmllKysxV0NmL1M3dFErOS0tOW5EYTgrMGtnd0hrSFpocDdjankzdz09--259a8b1c24f06508577aae0972a344ceac47c4f6; __hssc=70217615.5.1673402544285; __cf_bm=Xwj5ZSAfEQ4UfFYUKjj_zn2gvmvVg_pu9qe5WbK0zak-1673403601-0-AXs0tm7JGy9hHMWD423dPHLvSE3sMuIi6aDqcgT8YlzS4+5Z5t8pdrlnEpzfRjiyrIJ2o6enoSGDduoKJ1gWhWw=',
    'dnt': '1',
    'pragma': 'no-cache',
    'referer': 'https://www.xometry.com/quoting/quote/Q36-0160-6252/63be19d4d54e146933b66919?initialTab=Configure',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'id': 'tube-cutting',
    
}
# params = {
#     'id': 'tube-bending',
    
# }

response = requests.get(
    'https://www.xometry.com/api/requirements-service/2/menu',
    params=params,
    cookies=cookies,
    headers=headers,
)

# for item in reversed(l):
response = response.json()["items"]
# response = response['items']

import json 

json_str = json.dumps(response)

with open("xometory/cnc.json","w") as f:
    json.dump(response,f)
    f.close()
    
with open("xometory/cnc.json",'r') as f:
    load_dict = json.load(f)
    f.close()


##########
material = response['items'][0]['items'][0]['items']

color = response['items'][1]['items']
finish = response['items'][2]['items'][0]['items']

Finish_list = response
a = 1
# for material in material_list:
    