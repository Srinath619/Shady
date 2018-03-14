 def play_60():
	n=input('Enter string1 :')
	nn=input('Enter string2 :')
	for i in range(len(n)):
		if n[i]==nn[i]:
			return 'yes'
	return 'no'
play_60()
