n = int(input())
l = 3

if n > 1:
    for i in range(n-1):
        l = 2 * l - 1

print(l ** 2)
