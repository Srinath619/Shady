def play_56():
	a=input('Enter string :')
	aa=input('Enter char :')
	a1=list(a)
	for i in range(len(a1)):
		if a1[i]==aa:
			return i+1
	return -1
play_56()
