def play_74():
	a=input('Enter string :')
	l=list(a)
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if l[i]==l[j]:
				return 'Yes'
	return 'No'
play_74()
