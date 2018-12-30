line = input().split()
h = int(line[0])
m = int(line[1])

if m < 45:
    print((h-1) % 24, (m - 45) % 60)
else:
    print(h, (m - 45) % 60)
