
from peewee import *

db = MySQLDatabase('crm', host="localhost", user='root', passwd='123456', port=3306)
class company(Model):
    name = CharField()
    name_lower = CharField()
    company_url = CharField()
    localtion = CharField()
    industry = CharField()
    size = CharField()
    linkedin_url = CharField()
    linkedin_id= IntegerField()
    email_suffix = CharField()
    snov_id = CharField()
    source= CharField()
    # size = CharField()
    # birthday = DateField()
    # is_relative = BooleanField()

    class Meta:
        database = db


    def getcompany(start,end):
        
            
        c =  company().select().where((company.id >= start)&(company.id <= end))
        # c =  company_ta().select()
        return c

    def autosave():
        pass
        
        
        







    
