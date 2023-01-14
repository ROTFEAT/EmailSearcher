from pymysql import *
# from Twitter.twitter import *
def query_email(twitter_url):
    list = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,0,1,2,3,4,5,6,7,8,9".split(",")
    table_name = []
    for i in list:
        table_name.append(i+"_"+"twitter_raw") #给表格的名字赋值
    if twitter_url.startswith("@"):
        twitter_url = twitter_url.replace("@","")
    else:
        pass
    flag_name = twitter_url[0]
    try:
        index = list.index(flag_name.upper())
        table = table_name[index]
    except:
        table = "9_twitter_raw" 
    conn = connect(host='192.168.1.10', port=3306, user='root', password='123456', database='twitterdb', charset='utf8')
    cursor = conn.cursor()  # 获取光标
    sql = "SELECT `email`  FROM "+table +" WHERE `twitter_url`=%s Limit 1"
    cursor.execute(sql,(twitter_url))
    res = cursor.fetchone()[0]    
    conn.commit()
    return res
    # cs.close()
    # conn.close()

def update_email(id = None): 
    #1 查本地数据库
    conn = connect(host='127.0.0.1', port=3306, user='root', password='123456', database='twitter_user', charset='utf8')
    cursor = conn.cursor()  # 获取
    # sql = "select url from twitter_url where id>`%s`"
    if id!=None:
        sql = "select url from twitter_user where id > %s"
        cursor.execute(sql,(id))
    else:
        sql = "select url from `twitter_user` "
        cursor.execute(sql)
    res = cursor.fetchall()
    
    
    #2  查询返回结果并且更新
    count = 0
    for index,url in enumerate(res):
        try:
            url = url[0]
            email  = query_email(url) #i为url
            # twitter_update_breached_email(email=email,url=i)
            update_local(email,url=url)
            count = count + 1
            print(index,len(res),count)
            a = 1
        except:
            pass

def update_local(email,url):
    conn = connect(host='127.0.0.1', port=3306, user='root', password='123456', database='twitter_user', charset='utf8')
    cursor = conn.cursor() 
    sql = "UPDATE twitter_user SET breached_email = %s WHERE url = %s"
    val = (email, url)
    cursor.execute(sql,val)
    print("更新了",url)
    conn.commit()

if __name__ == "__main__":
    update_email()
    # res = query_email("2017M22_2")
    # update_email(200)
    a = 1