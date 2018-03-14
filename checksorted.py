n=int(input("How many elements??"))
s=[]
for x in range(n):
	k=int(input())
	s.append(k)
b=sorted(s)
if s==b:
	print("Yes")
else:
	print("No")
