import random
class negativeError(Exception):
	def __init__(self,num):
		Exception.__init__(self)
		self.num = num
x = 100.0
guess = round(random.uniform(0,x),4)
while True:
	try:
		num = float(input('Input a number within 100, \
it should have no more than 3 digits and I will guess it: '))
		if num < 0 or num > x:
			raise negativeError(num)
	except ValueError:
		print('The input must be a float or integer!')
		continue
	except negativeError as ne:
		print("{} is not a positive number or it's out range".format(ne.num))
		continue
	else:
		num = round(num,3)
		break
count = 0
guess = x/2
middle= x/4
while guess != num:
	if guess > num:
		guess -= middle
		print('I guess {}'.format(guess))
	else:
		guess += middle
		print('I guess {}'.format(guess))
	middle/= 2
	count += 1

print("Oh yeah! I got it. It's {}!".format(guess))
print('I totally used {} times'.format(count))