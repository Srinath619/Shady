try:
	s1=raw_input()
	a=s1.split(' ')
	b=" "
	for i in range(0,len(a)):
			a[i]=a[i].capitalize()
	c=a[0]
	for i in range(1,len(a)):
		c=c+b+a[i]
	print c
except:
	print "Invalid"
