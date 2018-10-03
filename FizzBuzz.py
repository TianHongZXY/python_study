for i in range(0,101):
	if i%3 != 0 and i%5!=0:
		print(i,end=',')
	elif i%3 == 0:
		if i%5 != 0:
			print('Fizz',end=',')
		else:
			print('FizzBuzz',end=',')
	elif i%5 == 0:
		print('Buzz',end=',')