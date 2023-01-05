from peewee import *

db = MySQLDatabase('crm', host="localhost", user='root', passwd='123456', port=3306)
class Company_ta(Model):
    name = CharField()
    name_lower = CharField()
    url = CharField()
    localtion = CharField()
    industry = CharField()
    size = CharField()
    linkedin_url = CharField()
    linkedin_id= IntegerField()
    snov_id = CharField()
    # size = CharField()
    # birthday = DateField()
    # is_relative = BooleanField()

    class Meta:
        database = db
    
    def save_to_db(self):
        pass



        




    
