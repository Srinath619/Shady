def play_55():
	n=input()
	l=n.split(' ')
	n1,n2=l[0],l[1]
	i=0
	a=''
	b='\0'
	while(i<len(n1)):
		if ord(n1[i]) in range(65,91):
			q=ord(n1[i])+32
			a=chr(q)
		if ord(n2[i]) in range(65,91):
			q=ord(n2[i])+32
			b=chr(q)
		if n1[i]==n2[i] or a==n2[i] or b==n1[i]:
			i+=1
		else :
			return 'No'
	return "yes"
play_55()
