def mul(m1,m2):
	mul=int(m1)*int(m2)
	return(str(mul))

def main():
	try:
		a=input()
		b=input()
		print(mul(a,b))
	except:
		print('invalid')
main()
