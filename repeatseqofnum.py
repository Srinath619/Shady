def play_68():
	a=int(input('Enter a:'))
	l,c,max=[],0,-1
	print('Enter elements :')
	for i in range(a):
		l.append(int(input()))
	for i in range(a):
		for j in range(i+1,a):
			if l[i]==l[j]:
				c+=1
		if max<c:
			max=c
		c=0
	print(max+1)
play_68()
