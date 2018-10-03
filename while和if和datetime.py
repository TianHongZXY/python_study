count = 0
while count<10:
    if count%2==0:
        print (count)
    count +=1
x= 7.0
y= 5
print(x%y)

m = 0
x = 1.047
i=1
while i<=10:
    m=(m+1000)*x
    i+=1
print(m)

import datetime
print(datetime.date.today())

x=1
y=-1
z=1
if x>0: #进入这个if 后面的elif就不进入了
    if y>0: print('aaa')
elif z>0:print('bbb')
