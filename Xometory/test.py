a = {"name:":{
    "title":{
        "aa":1,
        "bb":2,
    }
}
}
b = {"name:":{
    "title2":{
        "aa":1,
        "bb":2,
    }
}
}

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

list = ['Technology', 'Metal Binder Jetting', 'Material', '316i (316SS/Brz)', 'Finish', 'Zirblast']

from functools import reduce 
def list2tree(list):
    res = reduce(lambda x, y: {y: x}, reversed(list), {})
    return res

a = {"a":1,"v":1}
b = {"a":{"vb":2},"vb":2}

# a = {"name:",{}}
def dic2tree(dic,result):
    #输入dict 转为 tree 
    # result
    it = result
    dic_list = []
    for key,value in dic.items():
        
        dic_list.append(key)
        dic_list.append(value)

    new_dict  = list2tree(dic_list)
    dic = dict(it, **new_dict)
    result = dic
    return result
dict1 = {'Technology': {'Metal Binder Jetting':{'Metal Binder 122g':1}}}
# dict1 = {}
dict2 = {'Technology': {'Carbon Digital Light Synthesis (DLS)': {'Metal  122g':1}}}

# dict1 = {'a': 10, 'b': 8} 
# dict2 = {'d': 6, 'c': 4} 

def Merge(dict1, dict2): 
    return(dict2.update(dict1)) 

if __name__ == '__main__':
    # Merge(dict1=dict1,dict2 = dict2)
    # print(dict2)

    dict_update(dict1,dict2)
    res = 
    print(res)
    # res = dic2tree(a,b)
    # res = list2tree(list)
    # dict_1 = a
    # dict_2 =b
    # # dict_1.update(dict_2)
    # dict_update(dict_1, dict_2)
    # 啊 = dict_1
    # print(dict_1)


