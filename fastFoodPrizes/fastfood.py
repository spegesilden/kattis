def isCollectable(p, stickers):
    for i in range(len(p) - 1):
        if stickers[p[i]-1] == 0:
            return False
    return True

r = int(input())

for i in range(r):
    line = input().split()
    n = int(line[0])
    prizes = []
    result = 0

    for j in range(n):
        l = input().split()
        k = int(l[0])
        p = []
        for h in range(1, len(l)):
            p.append(int(l[h]))
        prizes.append(p)

    st = input().split()
    stickers = [int(s) for s in st]

    while len(prizes) > 0:
        for p in prizes:
            if isCollectable(p, stickers):
                for j in range(len(p)-1):
                    stickers[p[j]-1] -= 1
                result += p[-1]
            else:
                prizes.remove(p)

    print(result)
