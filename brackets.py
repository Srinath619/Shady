st1=input("Enter the brackets:")
r=[]
if st1[0]==')' or st1[len(st1)-1]=='(':
	print("Not valid")
elif st1.count('(')!=st1.count(')'):
      print("Not valid")
else:
    l=len(st1)
    for x in range(l):
        if st1[x]=='(':
            r.append(st1[x])
        elif st1[x]==')' and len(r)!=0:
            if r[len(r)-1]=='(':
                r.pop()
    if len(r)==0:
        print("Valid")
    else:
        print("Invalid")
