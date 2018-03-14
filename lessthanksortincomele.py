def play_64():
	a=int(input('Enter a:'))
	l=[]
	print('Enter elements :')
	for i in range(a):
		l.append(int(input()))
	k=int(input('Enter k:'))
	for i in range(a):
		if l[i]<k:
			print(l[i],end=" ")

play_64()
