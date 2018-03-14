def play_50():
	a=int(input('Enter a:'))
	for i in range(2,a//2):
		if n%i==0:
			return "yes"
	return "no"
  
play_50()
