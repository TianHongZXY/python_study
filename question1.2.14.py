import math
import random
#2计算sin^2+cos^2
a = float(input('Please input a rad: '))
x = math.sin(a)**2 + math.cos(a)**2
print(round(x,3))

#17掷骰子
a = random.randrange(1,7)
b = random.randrange(1,7)
print(a,b,a+b)

#20判断日期
m = int(input('month: '))
d = int(input('day: '))
if m>=4 and m<=5:
	print('True')
elif m==3 and d >=20:
	print('True')
elif m==6 and d <=20:
	print('True')
else:
	print('False')

#极坐标转换
x = float(input('x: '))
y = float(input('y: '))
p = round(math.sqrt(x**2 + y**2),4)
o = math.atan2(y,x)
o = math.degrees(o)
print('p={}\no={} degrees'.format(p,o))