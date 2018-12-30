import math

line = input().split()
n = int(line[0])
w = int(line[1])
h = int(line[2])
l = int(math.sqrt((w**2) + (h**2)))

for i in range(n):
    match = int(input())

    if match > l:
        print('NE')
    else:
        print('DA')
