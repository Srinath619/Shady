def play_75():
	a=int(input('Enter a:'))
	l,c=[],0
	print('Enter elements :')
	for i in range(a):
		l.append(int(input()))
	for i in range(a-1):
		for j in range(i+1,a):
			if l[i]<l[j]:
				c+=1
	print(c)
play_75()
