
lines = 0
with open("Text.txt", 'r') as f:
    for line in f:
        lines += 1
print("Number of lines:")
print(lines)
