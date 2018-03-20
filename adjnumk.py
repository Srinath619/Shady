def play_73():
	a=int(input('Enter a:'))
	l,max=[],-1
	print('Enter elements :')
	for i in range(a):
		l.append(int(input()))
	k=int(input('Enter k:'))
	for i in range(a):
		for j in range(i+1,a):
			if i==0:
				ans=l[i]-l[1]
			elif i==a-1:
				ans=l[i]-l[i-1]
			else :
				ans=l[i]-l[i-1]-l[i+1]
			if ans<0:
					ans=-ans
			if ans==k:
				return(l[i])
play_73()
