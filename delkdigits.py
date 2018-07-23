def leastdig():
	a=input()
	b=int(input())
	l=[]
	for i in a:
		l.append(i)
	l.sort()
	s=''
	g=len(l)-b
	for i in range(g):
		s=s+l[i]
	print(int(s))
try:
	leastdig()
except:
	print('invalid')
