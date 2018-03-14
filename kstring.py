def play_44():
	n=input('Enter string :')
	k=int(input('Enter k :'))
	d=n[k:]
	d+=n[:k]
	print(d)
  
play_44()
