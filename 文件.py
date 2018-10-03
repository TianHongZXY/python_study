poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
	use Python!
'''

# 打开文件以编辑（'w'riting）
f = open('poem.txt', 'w')
# 向文件中编写文本
f.write(poem)
# 关闭文件
f.close()

# 如果没有特别指定，
# 将假定启用默认的阅读（'r'ead）模式
f = open('poem.txt')
while True:
	line = f.readline()#每次只读当前一行,再指向下一行,但读到空行时并不会返回Null,所以要根据len()判断跳出循环
	# 零长度指示 EOF
	if len(line) == 0:
		break
	# 每行（`line`）的末尾
	# 都已经有了换行符
	#因为它是从一个文件中进行读取的
	print(line, end='')
f.close()

f = open('poem.txt')
lines = f.readlines() #返回列表类型
print(lines)
# 关闭文件
f.close()