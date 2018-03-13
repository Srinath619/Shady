def play_33():
	a=int(input('Enter a :'))
	c=0
	l=[[x for x in range(a)] for j in range(a)]
	print('Enter elements :')
	for i in range(0,a):
		for j in range(a):
			l[i][j]=int(input())
	for i in range(a):
		for j in range(1,a-1):
			if l[i][j]==1:
				if i==0 and (l[i][j+1]==0 and l[i][j-1]==0 and l[i+1][j]==0):
					c+=1
				elif i==a-1 and (l[i][j+1]==0 and l[i][j-1]==0 and l[i-1][j]==0):
					c+=1
				elif i!=0 or i!=a-1 and (l[i][j+1]==0 and l[i][j-1]==0 and l[i+1][j]==0 and l[i-1][j]==0):
					c+=1
	print('Count for island :',c)
  
play_33()
