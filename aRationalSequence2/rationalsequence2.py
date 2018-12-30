def number(p, q, d, r):
    if p == 1 and q == 1:
        return [d, r]

    if p - q > 0:
        parentP = p - q
        parentQ = q
        r += 2 ** d
        return number(parentP, parentQ, d + 1, r)
    else:
        parentP = p
        parentQ = q - p
        return number(parentP, parentQ, d + 1, r)

p = int(input())

for i in range(p):
    l = input().split()
    m = int(l[0])
    l2 = l[1].split('/')
    p = int(l2[0])
    q = int(l2[1])

    a = number(p, q, 0, 0)
    n = (2 ** a[0]) + a[1]

    print(m, n)
