url = "file:///url?esrc=s&q=&rct=j&sa=U&url=https://www.2g-eng.com/&ved=2ahUKEwi5pPGexZ78AhVvsFYBHeQAAtoQFnoECAgQAg&usg=AOvVaw3PCSQiR2VWgoklziwNjkxX"

import re 
  
def Find(string): 
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return url


a = Find(url)
print(a)
      