import logging
logging.basicConfig(filename='Assesment.log',level=logging.DEBUG)
def Additive(l,le):
    flag=0
    
    for i in range(le-2):
        if(l[i]+l[i+1]==l[i+2]):
            flag=1
        else:
            flag=0
    if flag==1:
        print("Additive")
    else:
        print("not additive")

if __name__=="__main__":
    l=input("Enter series in the form of [,,]:")
    logging.info('List is %s'%l)
    le=len(l)
    Additive(l,le)
