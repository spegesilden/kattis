x = int(input())
n = int(input())

used = 0
for i in range(n):
    used += int(input())

print(x*(n+1)-used)
