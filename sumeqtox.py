def play_61():
	a=int(input('Enter a:'))
	l=[]
	print('Enter elements :')
	for i in range(a):
		l.append(int(input()))
	k=int(input('Enter k:'))
	for i in range(a):
	      for j in range(i+1,a):
		      if l[i]+l[j]==k:
			      return 'yes'
	return 'no'
play_61()
