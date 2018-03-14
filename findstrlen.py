def play_53():
	a=input()
	a+='\0'
	c=0
	i=0
	while(True):
		if a[i]=='\0':
			break
		c+=1
		i+=1
	print(c)
play_53()
