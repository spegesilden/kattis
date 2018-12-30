n = int(input())
result = 0
for i in range(n):
    s = input()
    x = int(s[:-1])
    p = int(s[-1])
    result += x ** p
print(result)
