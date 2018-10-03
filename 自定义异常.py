# encoding=UTF-8

class ShortInputException(Exception):#自定义的异常必须继承异常类
	'''一个由用户定义的异常类'''
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	text = input('Enter something --> ')
	if len(text) < 3:
		raise ShortInputException(len(text), 3) #raise用于引起异常
	# 其他工作能在此处继续正常运行
except EOFError:
	print('Why did you do an EOF on me?')
except ShortInputException as ex:
	print(('ShortInputException: The input was ' + \
		'{0} long, expected at least {1}').format(ex.length, ex.atleast))
else:
	print('No exception was raised.')