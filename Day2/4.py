n1=0
n2=1
print(n1)
print(n2)

i=2
while(i<50):
	i=n1+n2
	if(i>50):
		break
	print(i)
	n1=n2
	n2=i
	i=i+1