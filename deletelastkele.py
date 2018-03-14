def play_69():
	r=int(input('Enter r:'))
	l,c=[],0
	print('Enter elements :')
	for i in range(r):
		l.append(int(input()))
	k=int(input('Enter k:'))
	for i in range(r-k,r):
		l.pop()
	print(*l)
play_69()
