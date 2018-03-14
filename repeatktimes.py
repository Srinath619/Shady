def play_66():
	s=int(input('Enter s:'))
	l,c=[],0
	print('Enter elements :')
	for i in range(s):
		l.append(int(input()))
	k=int(input('Enter k:'))
	for i in range(s):
		for j in range(i+1,s):
			if l[i]==l[j]:
				c+=1
		if c==k-1:
			print(l[i],end=" ")
		c=0
play_66()
