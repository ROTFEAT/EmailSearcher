import re
def find_link(string): 
    # findall() 查找匹配正则表达式的字符串
    # patten = "^((https|http|ftp|rtsp|mms)?:\/\/)[^\s]+"
    # patten= 'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+&ved'

    google_patten = "(https?://.*)&ved"
    url = re.findall(google_patten, string)
    return url[0]

def find_domain(string):
    patten= 'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    url = re.findall(patten, string)
    return url[0]



if __name__ =="__main__":
    s = "file:///url?esrc=s&q=&rct=j&sa=U&url=https://www.2g-eng.com/&ved=2ahUKEwi5pPGexZ78AhVvsFYBHeQAAtoQFnoECAgQAg&usg=AOvVaw3PCSQiR2VWgoklziwNjkxX"
    # s = "file:///url?esrc=s&q=&rct=j&sa=U&url=https://www.linkedin.com/company/2g-engineering&ved=2ahUKEwi5pPGexZ78AhVvsFYBHeQAAtoQFnoECAIQAg&usg=AOvVaw1IcnWNLrDTeNOqzPUEQkVc"
    
    url = find_link(s)
    print(url)
