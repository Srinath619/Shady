def play_76():
	a=int(input('Enter a:'))
	l,c1,c2=[],0,0
	print('Enter elements :')
	for i in range(a):
		l.append(int(input()))
	for i in range(a):
		if l[i]%2==0:
			c1+=1
			pos1=i
		else :
			c2+=1
			pos2=i
	if c1==a-1:
		print(l[pos2])
	elif c2==a-1:
		print(l[pos1])
play_76()
