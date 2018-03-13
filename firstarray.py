d=int(input("Enter the N value:"))
b=int(input("Enter the N value:"))
print("Enter your first array:")
a=[]
for x in range(d):
	m=int(input())
	a.append(m)
print("Enter K array:")
for x in range(b):
	m=int(input())
	a.append(m)
	print(max(a))
