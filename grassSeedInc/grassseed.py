c = float(input())
l = int(input())
cost = 0.0

for i in range(l):
    line = input().split()
    a = float(line[0])
    b = float(line[1])

    cost += a * b * c

print(cost)
