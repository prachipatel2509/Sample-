a=int(input("Input a dog's age in human years:"))
if(a>2):
    b=a-2
    b=b*4
    c=b+21
    print("The dog's age in dog's years is "+str(c))
elif(a==2):
    print("The dog's age in dog's years is 21")
else:
    print("The dog's age in dog's years is 10.5")
