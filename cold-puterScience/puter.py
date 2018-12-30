n = int(input())
result = 0

for t in input().split():
    if int(t) < 0:
        result += 1

print(result)
