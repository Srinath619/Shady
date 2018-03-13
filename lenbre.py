def circle(a):
	area=3.14*a*a
	print("Area  :", area)
  
def rectangle(l,b):
	area=l*b
	print("Area :",area)
  
def triangle(b,h):
	area=0.5*b*h
	print("Area  :",area)
def main():
	try:
		a=int(input("Enter radius for circle :\n"))
		circle(a)
		print("\n ----Rectangle----\n")
		l=int(input("Enter length :\n"))
		b=int(input("Enter breadth :\n"))
		rectangle(l,b)
		print("\n----Triangle---- \n")
		b=int(input("\nEnter Breadth  :\n"))
		h=int(input("Enter Height  :\n"))
		triangle(b,h)
	except:
		print('invalid')
main()
