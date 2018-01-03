
def is_triangle(a,b,c):
	check_1 = a>(b+c)
	check_2 = b>(a+c)
	check_3 = c>(a+b)
	if (check_1 or check_2 or check_3):
		print("NO")
	else:
		print("YES")


a = int (input("enter a: "))
b = int (input("enter b: "))
c = int (input("enter c: "))

is_triangle(a,b,c)