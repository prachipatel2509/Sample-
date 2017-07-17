
def sequence(x):
    l = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
    
       l.append(x)    
    return l

if __name__=="__main__":
    n=int(input("Enter a no. :"))
    print(sequence(n))
