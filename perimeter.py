def play_45():
	n=int(input('Enter n :'))
	a=int(input('Enter A :'))
	s=int(a**0.5)
	if float(s)==float(a**0.5):
		if int(a**(0.5))==(n//4) :
			return('Yes')
	return('No')
play_45()
