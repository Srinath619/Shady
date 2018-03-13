def uniq(string):
	a=[]
	for i in range(len(string)):
		if string[i] in a:
			continue
		a.append(string[i])
	print(''.join(a))
def main():
	str=input()
	uniq(str)
main()
 
