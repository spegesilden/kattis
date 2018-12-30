n = int(input())
s = 0

for i in input().split():
    if int(i) < 0:
        n -= 1
    else:
        s += int(i)

print(float(s/n))
