n=int(input('输入任意一个整数:'))
#for n in range(27,100):
while n!=1:
    if n%2==0:
          n/=2
    else:
        n=3*n+1
    print (n)
