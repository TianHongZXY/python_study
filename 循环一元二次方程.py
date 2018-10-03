import math as m

ch = ''

while ch !='q':
    a = float(input('please input a:'))
    b = float(input('please input b:'))
    c = float(input('please input c:'))
    delta = b**2 - 4*a*c
    if a ==0:
        print('x=',-c/b)
    elif delta<0:
        print('no solution')
    else:
        print('x1=',(-b+m.sqrt(delta))/(2*a),'x2=',(-b-m.sqrt(delta))/(2*a))
    ch = input('终止请输入q:')
os.system("pause")
