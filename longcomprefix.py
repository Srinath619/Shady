def longcomstr(l):
	a=l[0]
	b=''
	n=len(a)
	for i in range(1,len(l)):
		for j in range(0,len(l) and n):
			if a[j]!=l[i][j]:
				break
			b=b+a[j]
	print(b)
def main():
	try:
		strarr=input()
		l=strarr.split()
		longcomstr(l)
	except:
		print('invalid')
    
main()
