
import json
from xometory.bainli import *

with open("xometory/cnc.json",'r') as f:
    load_dict = json.load(f)
    response =load_dict['items']
    load_dict =load_dict['items']
    f.close()

# def ()

lable_list = []
for value in response:
    lable_list.append(value["label"]) #有可能为空

#直接用list创建变量 生成待处理数据emrlable_list
for index,value in  enumerate(lable_list):
    if value == "Material":
        globals()[value] =[]
        material_types = response[index]['items'][0]['items']
        # response[0]['items'][0]['items']
        for material in material_types:
            for j in material["items"]:
                globals()[value].append(j)
    
    if value == "Color":
        # globals()[value] =[]
        globals()[value] = response[index]['items']
        pass
    
    if value =="Finish":
        # globals()[value]
        finish_type = response[index]['items'][0]['items']
        fin_taged = {}
        for i  in finish_type:
            try:
                for j in i["items"]:
                    for z in j['displayWhen']['tagged']:
                        try:
                            fin_taged[z].append(j["label"])
                        except:
                            fin_taged[z] = [j["label"]]
            except:
                continue
        globals()[value] =fin_taged
    
    if value == "Tolerance":
        globals()[value] = response[index]['items'][0]['items']
        temp = []
        for i in globals()[value]:
            temp.append(i["label"])
        globals()[value] = temp

    if value == "Surface Roughness":
        globals()[value] = response[index]['items'][0]['items']
        temp = []
        for i in globals()[value]:
            temp.append(i["label"])
        globals()[value] = temp
      
    # if value == "Surface Roughness":
    #     globals()[value] = response[index]['items'][0]['items']

tree = [] #生成树
for value in lable_list:
    try: 
        globals()[value]
        tree.append(value)
    except:
        continue

for key,value in Finish.items():
    globals()[key] = value



res = {
    
}

for value in tree:
    for i in globals()[value]:
        res[i["label"]] = {}
        tags = i["tags"]
        for j in tags:
            
            
            a = res[i["label"]]["Finish"] 
            pass
            

        # res[i["label"]][]




    a  = 1
    # try:
    #     res[]
    # except:

    #     pass
