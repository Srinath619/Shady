import math

a,b =input().split()
a=int(a)
b=int(b)
print(type(a))
count=0
for q in range(a,b):
  if int(math.sqrt(q))**2==q:
      count=count+1
print(count) 
