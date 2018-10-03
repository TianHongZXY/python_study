import winsound
from time import sleep, localtime
#count = 0
def beep(m):
	if m == 0:
		for i in range(1,3):
			winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
		print("It's ")
		return True
	elif m == 30:
		for i in range(1,3):
			winsound.PlaySound('*', winsound.SND_ALIAS)
		print("It's 30 now.")
		return True
	#global count
	#count += 1
if __name__ == '__main__':
	while True :
		now = localtime()
		m = now.tm_min
		s = now.tm_sec
		#beep(m)
		if beep(m):
			sleep(60*29)
			

