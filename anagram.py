def lastjump(a,n):
	i=0
	while i<n:
		i+=a[i]
		try:
			if i==a[i]:
				return True
		except:
			return False
      
def main():
	a=[]
	n=int(input())
	for i in range(n):
		a.append(int(input()))
	print(lastjump(a,n))

main()
