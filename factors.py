import random
sum = 0
n = int(input())
for i in range(10):
	x = 0
	y = 0
	step = 0
	while (x**2)<4*(n**2) or (y**2)<4*(n**2):
		p = random.random()
		if p<=0.25:
			x += 1
		elif p<=0.5:
			x -= 1
		elif p<=0.75:
			y += 1
		else:
			y -= 1
		step += 1
	sum += step
	print('total {} steps'.format(step))
average = sum/10
print('average = {} steps'.format(average))