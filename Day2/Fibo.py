#fibonacci
n1=0
n2=1
print(n1)
print(n2)

i=2
while(i<50):
	i=n1+n2 # add first and second element (a=0 ,b = 1 then print 1)
	if(i>50):
		break
	print(i)
	n1=n2 # make a=1
	n2=i 3 #make b=1
	i=i+1 #i=3
