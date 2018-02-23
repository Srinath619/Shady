def rotate(a,k,l):
	r=[]
	for i in range(a-k,n):
		r.append(l[i])
	for i in range(a-k):
		r.append(l[i])
	print(r)
def main():
	try:
		a=int(input())
		k=int(input())
		l=[]
		for i in range(a):
			l.append(int(input()))
		rotate(a,k,l)
	except:
		print('invalid')
main()
