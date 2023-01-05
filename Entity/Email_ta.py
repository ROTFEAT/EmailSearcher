from peewee import *

db = MySQLDatabase('crm', host="localhost", user='root', passwd='123456', port=3306)
class email_snov(Model):
    email_addr = CharField()
    name = CharField()
    company_name = CharField()
    title = CharField()
    emailid = IntegerField()
    indb_time = CharField() #不用填写
    keyword = CharField() #看着办
    industry = CharField() 
    email_state = CharField() 
    last_send_time = DateField() #保留不填
    fist_send_time = DateField() #保留不填
    frequency= IntegerField() #发送次数
    opened_times= IntegerField() #打开次数
    snov_id = CharField()
    linkedin_url = CharField()
    compare = CharField()
    userstate = CharField()
    country = CharField()
    email_type = CharField()
    
    # size = CharField()
    # birthday = DateField()
    # is_relative = BooleanField()

    class Meta:
        database = db
    
    def sava_to_db(self,ins):
        try:
            ins.save()
        except:
            pass





    
