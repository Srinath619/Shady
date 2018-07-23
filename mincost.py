def g(a,b):
	p=0
	q=''
	r=0
	f=0
	for i in range(len(a)):
		if len(a)<len(b):
			if a[i]==b[i]:
				q+=a[i]
				p=p+1
		else :
			f=1
			break
	i=0
	if f==1:
		while(True):
			if a[i]==b[i]:
				q+=a[i]
			else :
				q+=b[i]
				r=r+1
			if i==3:
				break
			i=i+1
		return r

	for i in range(p,len(b)):
		q+=b[i]
		r=r+1
	return r
 
 def main():
	a=input()
	b=input()
	print(g(a,b))
try:
 	 main()
except:
 	 print('invalid')
