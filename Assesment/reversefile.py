filename="Text.txt"

for line in reversed(list(open(filename))):
    print(line.rstrip())
