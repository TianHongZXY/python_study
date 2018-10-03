import re
relink = '<a href="(.*)">(.*)</a>'#如果加了括号 则只返回匹配括号内的内容列表
info = '<a href="http://www.baidu.com">baidu</a>'
cinfo = re.findall(relink,info)
relink1 = '<a href=".*">.*</a>'
cinfo1=re.findall(relink1,info)#如果不加括号 则返回匹配的含整个字符串的列表
print(cinfo)
print(cinfo1)
