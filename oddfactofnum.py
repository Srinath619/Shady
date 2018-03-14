def play_48():
	a=int(input('Enter a:'))
	for i in range(2,a//2):
		if a%i==0 and i%2!=0:
			print(i,end="\t")
      
play_48()
