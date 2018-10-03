def move(n,a,b,c):
	if n == 1:
		print(a,'->',c)
		return
	move(n-1,a,c,b)#将a柱子上除了最大的移动到b柱子
	move(1,a,b,c)#将最大的移动到c
	move(n-1,b,a,c)#将b柱子上的移动到c柱子上
move(3,'a','b','c')