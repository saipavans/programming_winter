def check_fermat(a,b,c,n):
	if ((a**n + b**n) == (c**n)) and n>2:
		print("fermat is correct")
	else:
		print("Holy smokes, Fermat was wrong")


a = int(input("enter a "))
b = int(input("enter b "))
c = int(input("enter c "))
d = int(input("enter d "))

check_fermat(1,2,3,3)