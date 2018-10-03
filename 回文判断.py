def reverse(text):
	return text[::-1]
def is_palindrome(text):
	return text == reverse(text)
while True:
	forbid = (',','.','"',"'",':',';','?','!','>','<',"\\",'','*',' ')
	something = input("Enter text: ")
	sl = something.lower()
	raw_string = []
	if sl == 'q':
		break
	else:
		for i in range(len(sl)):
			if sl[i] not in forbid:
				raw_string.append(sl[i])
		string = ''.join(raw_string)
		if is_palindrome(string):
			print("Yes, it is a palindrome")
		else:
			print("No, it is not a palindrome")
