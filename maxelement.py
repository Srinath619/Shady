def play_72():
	a=int(input('Enter a:'))
	l,max=[],-1
	print('Enter elements :')
	for i in range(a):
		l.append(int(input()))
	for i in range(a-1):
		for j in range(i+1,a):
			if l[i]<l[j]:
				break
			else :
				if l[i]>l[j]:
					if max<l[i]:
						max=l[i]
				break
	print(max)
play_72()
