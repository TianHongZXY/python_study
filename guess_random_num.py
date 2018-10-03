import random

r = int(random.uniform(0,100))

while True:
	try:
		g = int(input('I have got a number within 100, please guess: '))
	except ValueError:
		print('The input must be a integer!')
		continue
	if g == r:
		print('Congratulations! You are right!')
		break
	elif g>r:
		print('Too big')
	else:
		print('Too small')