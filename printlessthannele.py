def play_65():
	e=int(input('Enter e:'))
	l=[]
	print('Enter elements :')
	for i in range(e):
		l.append(int(input()))
	for i in range(e):
		if l[i]<n:
			print(l[i],end=" ")
play_65()
