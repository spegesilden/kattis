def loadCars(L, q):
    newq = q[::]
    if len(newq) == 0:
        return []
    elif newq[0] > L:
        del newq[0]
    l = 0
    while len(newq) > 0 and l + newq[0] <= L:
        l += newq[0]
        del newq[0]
    return newq

c = int(input())

for i in range(c):
    result = 0
    left = []
    right = []

    line = input().split()
    L = int(line[0])*100

    for j in range(int(line[1])):
        li = input().split()
        if li[1] == 'left':
            left.append(int(li[0]))
        else:
            right.append(int(li[0]))

    side = 'l'

    while len(left) > 0 or len(right) > 0:
        if side == 'l':
            left = loadCars(L, left)[::]
            side = 'r'
        else:
            right = loadCars(L, right)[::]
            side = 'l'
        result += 1

    print(result)
