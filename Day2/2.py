a = int(input("Enter degree of temperature:\n 1. Celcius\n2. Fahrenheit\n"))
if(a==1):
	b=float(input("Enter Temperature:"))
	c=(b*(9.0)/5)+32
	print(c)
elif(a==2):
	d=float(input("Enter Temperature:"))
	e=(d-32)*(5.0/9)
	print(e)
