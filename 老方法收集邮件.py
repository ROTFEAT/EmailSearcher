
from Entity.Company_ta import *
from Entity.Email_ta import *
from Entity.Email_ta_off import *

from RequestBody.SnovTask import *
from RequestBody.SnovCompanyList import *
from RequestBody.SnovEmaillist import *

from RequestBody.SnovEmaillist import *
from RequestBody.utils.email_filter import *

if __name__ == "__main__":
    countrylist = [
    "United States",
    "United Kingdom",
    "Germany",
    "Canada",
    "Luxembourg",
    "Switzerland",
    "Norway",
    "Iceland",
    "Denmark",
    "Sweden",
    "Netherlands",
    "Finland",
    "Austria",
    "Belgium",
    "San Marino",
    "France",
    "Andorra",
    "Italy",
    "Malta",
    "Spain",
    "Slovenia",
    "Estonia",
    "Cyprus"
    "Ireland",
    ]
    industrylist =[
        # "Transportation Equipment Manufacturing",
        # "Measuring and Control Instrument Manufacturing",
        # "Metal Valve, Ball, and Roller Manufacturing",
        # "Metalworking Machinery Manufacturing",
        # "Railroad Manufacture",
        # "Communications Equipment Manufacturing",
        # "Industrial Automation",
        # "Mechanical Or Industrial Engineering",
        # "Electrical Equipment Manufacturing",
        # "Engines and Power Transmission Equipment Manufacturing",
        # "Shipbuilding"
        # "Shipbuilding",  
        # "Machinery"
        # "Office Furniture and Fixtures Manufacturing",
        # "Electronic and Precision Equipment Maintenance",
        # "Commercial and Industrial Machinery Maintenance",
        # "Commercial and Service Industry Machinery Manufacturing",
        # "Agriculture, Construction, Mining Machinery Manufacturing",
        # "Medical Device",
        # "Transportation Equipment Manufacturing",
        # "Office Furniture and Fixtures Manufacturing",
        # "Electronic and Precision Equipment Maintenance",
        # "Commercial and Industrial Machinery Maintenance",
        # "Commercial and Service Industry Machinery Manufacturing",
        # "Agriculture, Construction, Mining Machinery Manufacturing",
        # "Medical Device",
        "Waste Treatment and Disposal",
        "Water Supply and Irrigation Systems",
        "Space Research and Technology",
        "Mattress and Blinds Manufacturing",
        "Electric Lighting Equipment Manufacturing",
        "Boilers, Tanks, and Shipping Container Manufacturing",
        "Audio and Video Equipment Manufacturing",
        "Architectural and Structural Metal Manufacturing",
        "Rail Transportation"
        ]
    company_count = 0
    for countrylist_instant in countrylist:
        for industrylist_instant in industrylist:
            m_locality = countrylist_instant
            m_industries = industrylist_instant
            task =  Task(locality=m_locality,industries=m_industries)
            taskid = task.get_task_id()['data']['taskId'] #获得id
            print("------------------等待返回-------------------")
            print("地点：",m_locality,"   ","行业:",m_industries)
            time.sleep(180)
            
            # taskid = 78363
            cl = Companylist()
            cl.settaskid(taskid)
            cl = cl.getcompanylist()
            
            startpage = 0 #起始页
            count = cl["count"]
            print("总数:",count,"行业：",m_industries,"国家：",m_locality)

            if count>=5000: #记录
              with open("log.txt","a") as file:   #”w"代表着每次运行都覆盖内容
                file.write(str(m_locality) +" "+str(m_industries)+ "d" + " "+"\n")

                file.close()

            endpage = int((count/25)+0.99)

            while(startpage<=endpage):
                print("this page:",startpage)
                company = Companylist()
                company.settaskid(taskid)
                company.setpage(startpage)
                
                cl = company.getcompanylist()
                companylist  = cl["data"]
                startpage = startpage+1
                for company in companylist:
                    company_snov_id = company["id"] #公司id snovid
                    company_name = company['name'] #公司名 

                    print("公司名字",company_name)
                    lower_company_name =company_name.lower() #小写公司名
                    websiet = company['url'] #公司网址  
                    localtion = company['location'] #公司地址
                    industry = company['industry'] #公司产业
                    companysize = company['size'] #公司规模
                    linkedin_url = ""
                    linkedin_id = ""
                    if company['social'][0]['type']=='linkedIn': #保存公司linkedin地址
                        social = company['social'][0]
                        linkedin_url = social["link"]
                        linkedin_id = linkedin_url.replace('https://www.linkedin.com/company/',"")
    
                    #数据库插入公司信息
                    c = Company_ta(name =company_name,name_lower = lower_company_name,url = websiet,localtion =localtion,industry =industry,size = companysize ,linkedin_url = linkedin_url,linkedin_id = linkedin_id,snov_id =company_snov_id)
                    try:

                        
                        c.save()#插不进去就不插了
                        company_count = company_count+1
                        print("抓取的公司数量:",company_count)

                        
                        snovemaillist = SnovEmaillist()
                        
                        emails = snovemaillist.getemail(company_snov_id)
                        a = 1
                        for email in emails:
                            emailaddr = email['email'] #邮件地址
                            name = email['local_part'] #邮件名
                            company_name = lower_company_name #公司名字
                            email_id = email['id'] #内部id
                            title = ""
                            country  = localtion.split(',')[-1].strip()
                            try:
                                if email_filter(email=emailaddr):
                                    if check_offical(email= emailaddr):
                                        c = email_off(email_addr =emailaddr ,name = name ,company_name = company_name,title =title,emailid =email_id ,keyword =" ",industry = industry,email_state = "未发送",frequency = 0,snov_id = company_snov_id,linkedin_url = "",userstate = "未询盘",country = country,opened_times=0,email_type = "抓取")
                                    else:
                                        c = email_snov(email_addr =emailaddr ,name = name ,company_name = company_name,title =title,emailid =email_id ,keyword =" ",industry = industry,email_state = "未发送",frequency = 0,snov_id = company_snov_id,linkedin_url = "",userstate = "未询盘",country = country,opened_times=0,email_type = "抓取")  
                                    try:
                                        c.save()
                                    except:
                                        continue
                            except:
                                print("邮件过滤报错")
                    except:
                        from datetime import datetime                        
                        print(datetime.now()," ","公司重复插入")
                        continue



