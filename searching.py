d=int(input("Enter N value:"))
b=int(input("Enter K value:"))
print("Enter your array:")
a=[]
for x in range(d):
	m=int(input())
	a.append(m)
if b in a:
	print("Yes")
else:
	print("No")
