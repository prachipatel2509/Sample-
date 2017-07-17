class Error(Exception):
    pass
class Weak(Error):
    pass
class Good(Error):
    pass

num=8

try:
    num1=raw_input("Enter password:")
    l=len(num1)
    if l<num:
        raise Weak
    elif l>num:
        raise Good
            
except Weak:
    print("Password is weak")
except Good:
    print("Good password")
