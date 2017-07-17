a=raw_input("Enter a string: ")

with open("Text.txt","a") as f:
    f.write(a)
