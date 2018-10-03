import sys
import time

f = None
try:
	f = open("poem.txt")
	# 我们常用的文件阅读风格
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print(line, end='')
		sys.stdout.flush() #刷新刚刚的输出 在windows下有没有都一样，
							#在Linux下若没有此行则只有循环结束才刷新所有输出
		print("Press ctrl+c now")
		# 为了确保它能运行一段时间
		time.sleep(2)
except IOError:
	print("Could not find file poem.txt")
except KeyboardInterrupt:
	print("!! You cancelled the reading from the file.")
finally:
	if f:
		f.close()
	print("(Cleaning up: Closed the file)")