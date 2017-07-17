"""Sum of digits"""

sum=0
i=1
n=int(input("Enter a 3 digit no. "))
while(i<= 3):
    n1=n%10
    sum=sum+n1
    n=n/10
    i=i+1
    
print(sum)
        
