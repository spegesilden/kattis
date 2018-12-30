def isSum(s, x, y):
    a = x + y
    while a < s:
        a += x
        i = 0
        while a < s and i < 1:
            a += y
            i += 1
    return s == a

s = int(input())

print(str(s) + ':')

for x in range(2,int(s/2)+2):
    for y in range(x-1,x+1):
        if isSum(s, x, y):
            print(str(x) + ',' + str(y))
