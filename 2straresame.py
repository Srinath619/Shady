 def play_54():
	a=input()
	l=a.split(' ')
	a1,a2=l[0],l[1]
	i=0
	while(i<len(a1)):
		if a1[i]==a2[i]:
			i+=1
		else :
			return 'No'
	return "yes"
play_54()
