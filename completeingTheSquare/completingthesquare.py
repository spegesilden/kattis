x = []
y = []
l = []

for i in range(3):
    line = input().split()
    x.append(int(line[0]))
    y.append(int(line[1]))

l.append(((x[0] - x[1]) ** 2) + ((y[0] - y[1]) ** 2))
l.append(((x[1] - x[2]) ** 2) + ((y[1] - y[2]) ** 2))
l.append(((x[2] - x[0]) ** 2) + ((y[2] - y[0]) ** 2))

if l[0] == l[1]:
    x.append(x[2] + x[0] - x[1])
    y.append(y[2] + y[0] - y[1])
elif l[1] == l[2]:
    x.append(x[0] + x[1] - x[2])
    y.append(y[0] + y[1] - y[2])
else:
    x.append(x[1] + x[2] - x[0])
    y.append(y[1] + y[2] - y[0])

print(x[3], y[3])
