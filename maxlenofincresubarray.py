def play_77():
	x=int(input('Enter x:'))
	l=[]
	print('Enter elements :')
	for i in range(x):
		l.append(int(input()))
	for i in range(x-1):
		for j in range(i+1,x):
			if l[i]<l[j]:
				m=l[j]
			break
	print(m)
play_77()
