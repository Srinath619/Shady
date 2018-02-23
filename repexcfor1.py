def count(str):
	(max,c)=(-1,0)
	a=[]
	for i in range(len(str)):
		if str[i] in a:
			continue
		a.append(str[i])
		for j in range(len(str)):
			if str[i]==str[j] :
				c=c+1
		if c==1:
			print(str[i])
		c=0
def main():
	try:
		n=int(input())
		l=[]
		for i in range(n):
			l.append(int(input()))
		count(l)
	except:
		print('invalid')
main()
