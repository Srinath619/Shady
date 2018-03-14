def play_57():
	b=input('Enter string :')
	bb=input('Enter char :')
	b1=list(b)
	c=0
	for i in range(len(b1)):
		if b1[i]==bb:
			c+=1
	return c
play_57()
