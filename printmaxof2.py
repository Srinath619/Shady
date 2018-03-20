def play_71():
	a=int(input('Enter a:'))
	l,c=[],0
	print('Enter elements :')
	for i in range(a):
		l.append(int(input()))
	for i in range(a-1):
		for j in range(i+1,a):
			if l[i]>l[j]:
				print(l[i],end=' ')
			else :
				print(l[j],end=' ')
			break
play_71()
