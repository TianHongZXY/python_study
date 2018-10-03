import requests
kv = {'user-agent':'chrome/10'}
url = input('输入你想要爬取的文件的URL: ')
r = requests.get(url,headers = kv)
if(r.status_code==200):
    print('爬取成功！')
else:
    print('爬取失败！')
path = input('输入你想存储的相对路径（将存在D盘python_spider中): ')
#r.request.headers
try:
    with open('D:/python_spider/' + path,'wb') as f:
        f.write(r.content)
except:
    print('路径错误！')
else:
    print('存储成功！')
f.close()
