""" Input:Tuples as input
Store it in list
Output:Sorted list of tuples in ascending order of last element of tuple
Logic:

"""

def last(n):
    return n[-1]  
 
def sort(tuples):
    return sorted(tuples, key=last)
 
a=input("Enter a list of tuples:")
print("Sorted:")
print(sort(a))
    
             
             
                
