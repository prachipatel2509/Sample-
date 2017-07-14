#Coverts Celcius to fahrenheit and fahrenheit to celcius
import logging

logging.basicConfig(filename='Day2.log',format='%(asctime)s-%(message)s',level=logging.DEBUG)
a = int(input("Enter degree of temperature:\n 1. Celcius\n2. Fahrenheit\n"))
logging.info('Value entered by user is:%d'%a)

if(a==1):

	b=float(input("Enter Temperature:"))
	c=(b*(9.0)/5)+32
	print(c)
elif(a==2):
	d=float(input("Enter Temperature:"))
	e=(d-32)*(5.0/9)
	print(e)
else:
        print("Please enter a valid Option")
