from peewee import *

db = MySQLDatabase('twitter_user', host="localhost", user='root', passwd='123456', port=3306)

# 定义Person
class twitter_user(Model): 
    name = CharField(100)   
    url = CharField(60)
    breached_email = CharField(60)
    content_email = CharField(60)
    content = TextField()
    source = CharField(60)
    class Meta:
        database = db
    
    
    # incon = DateField()
    # is_relative = BooleanField()

def creattable():
    twitter_user.create_table()

def inert2twitter(name,url,breached_email,content_email,content,source):
    tw = twitter_user(name = name,url = url,breached_email = breached_email,content_email = content_email,content = content,source = source)
    try:
        tw.save()
        print("插入url",url)
    except:
        pass



# # from Twitter.twitter import *
# def twitter_update_breached_email(email,url):

#     # q = twitter_user.update(twitter_user.breached_email=email).w 
#     # q.execute()
#     # twitter_user.update(twitter_user.breached_email : email).where(twitter_user.url == url)



if __name__ =="__main__":
    creattable()
    
