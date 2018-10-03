from turtle import *
def curvemove():
    for i in range(200):
        right(1)
        forward(1)
color('red','pink')        
begin_fill()
left(140)#左转140度
forward(111.65)#走111.65像素
curvemove()#顺时针转圈200度
left(120)
curvemove()
forward(111.65)
end_fill()
done()
