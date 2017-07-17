""" Program o print alphabet traingle
A
B C
D E F
G H I J
K L N M O
"""
inc=1
ch=65
for i in range(0,6):
    for j in range(0,inc):
        cha=chr(ch)
        print(cha),
        ch=ch+1
    inc=inc+1
    
    print
