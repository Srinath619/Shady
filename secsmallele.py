s=int(input("How many elements??"))
print("Enter th elements....")
a=[]
for x in range(s):
	k=int(input())
	a.append(k)
a.sort()
print("Second smallest number is:",a[1])
