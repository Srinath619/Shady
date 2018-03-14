def play_63():
	a=int(input('Enter a:'))
	l,m=[],[]
	print('Enter elements-1 :')
	for i in range(a):
		l.append(int(input()))
	print('Enter elements-2 :')
	for i in range(a):
		m.append(int(input()))
	for i in range(a):
		if l[i]==m[i]:
			print(l[i],end=" ")
play_63()
