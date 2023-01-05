
import re 
from Entity.Company_ta import *
from Entity.Email_ta import *
from Entity.Email_ta_off import *
def email_filter(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email): #查询是否满足条件
        if delete_email(email):
            return email
        else:
            return None
    else: 
        return None

def delete_email(email):
    regex = "(^.*)@"
    name = re.findall(regex,email)
    name = name[0]
    NotTrash = True
    if '..' in name:
        NotTrash = None

    if (len(name)<=2)|(len(name)>22): #排除长度不符合的邮箱
        NotTrash = None

    if (name =='22')| (name=='9D')| (name=='cs')| (name=='2a')| (name=='cs')| (name=='e')| (name=='ed'):
        NotTrash = None

    if 'xxx' in name:
        NotTrash= None

    tempname = name
    tempname = tempname.replace("-","").replace(".","").replace("_","").strip()
    if tempname.isdigit(): #全是数字 全是数字 就删除
        NotTrash= None

    if 'www.' in name:
        NotTrash = None
    
    return NotTrash


def check_offical(email):
    regex = "(^.*)@"
    name = re.findall(regex,email)
    name = name[0]
    keywordlist = 'office/info/service/sale/team/contact/support/office/info/service/sales/team/contact/support/HR/webposter/pr/service/websales/jobs/salesmanager/global/admin/accounting/ceo/website/hr/help/yourself/myself/account/web/quote/request/response/shop/Service/vip/resume/result/reception/quote/order/of/no-reply/market/last/tool/internation/inquiryimport/http/master/technology/host/tech/custserv/Customer/email/employ/enquir/first/seconed/thired/forth/fifth/acount/news/price/shipping/solution/used/international/table'.lower()
    name = name.lower()
    keywordlist = keywordlist.split('/')
    offcial = False
    for keyword in keywordlist:

        if keyword in name:
            offcial = True
            return True
        else:
            pass
    return False

if __name__  =="__main__":
    emailaddr = "info@qq.com"
    # name =
    if email_filter(email=emailaddr):#验证有效性
        if check_offical(email= emailaddr):
            print("官方")
            # c = email_off(email_addr =emailaddr ,name = name ,company_name = company_name,title =title,emailid =email_id ,keyword =" ",industry = industry,email_state = "未发送",frequency = 0,snov_id = company_snov_id,linkedin_url = "",userstate = "未询盘",country = country,opened_times=0,email_type = "抓取")
        else:
            print("非官方")
            # c = email_snov(email_addr =emailaddr ,name = name ,company_name = company_name,title =title,emailid =email_id ,keyword =" ",industry = industry,email_state = "未发送",frequency = 0,snov_id = company_snov_id,linkedin_url = "",userstate = "未询盘",country = country,opened_times=0,email_type = "抓取")  
        # try:
        #     # c.save()
        # except:
        #     pass