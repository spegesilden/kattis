def greater(a, b):
    c = a - b
    if c > 0:
        return a
    return b

line = input().split()
a = int(line[0])
b = int(line[1])
l = greater(a, b)

print(str(l)[::-1])
