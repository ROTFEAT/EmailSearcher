fo = open(r"ChromePortable64\2.txt", "r+")
print ("文件名为: ", fo.name)

line = fo.read(10)
print("读取的字符串:",line)

# 关闭文件
fo.close()