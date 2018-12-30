def empty(B, N):
    x = N[0]
    y = N[1]
    node = N[:]
    n = len(B)
    m = len(B[x])
    offsets = []

    if x < n - 2:
        offsets.append([2,0,1,0])
        if y < m:
            offsets.append([2,2,1,1])
    if x > 1:
        if y > 1:
            offsets.append([-2,-2,-1,-1])
        if y < m - 2:
            offsets.append([-2,0,-1,0])
    if y < m - 2:
        offsets.append([0,2,0,1])
    if y > 1:
        offsets.append([0,-2,0,-1])

    for o in offsets:
        if B[x+o[0]][y+o[1]] == '_' and B[x+o[2]][y+o[3]] != '_':
            node.append(o)

    return node

def makeQueue(B):
    Q = []

    for i in range(len(B)):
        for j in range(len(B[i])):
            if B[i][j] != '_':
                node = empty(B, [i, j])
                if len(node) > 2:
                    Q.append(node)

    return Q

def hasWon(B, t):
    pegs = 0
    for r in B:
        for c in r:
            if c != '_':
                pegs += 1
    if pegs == 1:
        for r in B:
            for n in r:
                if n == t:
                    return True
    return False

def isWinable(B, Q, t, tn):
    if tn == 0:
        return False

    if len(Q) == 0:
        return hasWon(B, t)

    b = False

    for n in Q:
        for i in range(2, len(n)):
            #newB = []

            if B[n[0]+n[i][2]][n[1]+n[i][3]] == t:
                tn -= 1

            old1 = B[n[0]][n[1]]
            old2 = B[n[0]+n[i][0]][n[1]+n[i][1]]
            old3 = B[n[0]+n[i][2]][n[1]+n[i][3]]


            B[n[0]+n[i][0]][n[1]+n[i][1]] = B[n[0]][n[1]]
            B[n[0]+n[i][2]][n[1]+n[i][3]] = '_'
            B[n[0]][n[1]] = '_'
            #newB[n[0]+n[i][0]][n[1]+n[i][1]] = newB[n[0]][n[1]]
            #newB[n[0]+n[i][2]][n[1]+n[i][3]] = '_'
            #newB[n[0]][n[1]] = '_'


            newQ = makeQueue(B)

            #for r in newB:
            #    print(r)
            #print('Queue Q:', Q)
            #print('Queue newQ:', newQ)

            b = b or isWinable(B, newQ, t, tn)

            B[n[0]][n[1]] = old1
            B[n[0]+n[i][0]][n[1]+n[i][1]] = old2
            B[n[0]+n[i][2]][n[1]+n[i][3]] = old3

    return b

t = input()[0]

while t != '*':
    B = [[input().split()[0][0]]]
    tn = 0

    for i in range(4):
        row = input().split()[0][::2]
        B.append([c for c in row])
        for c in row:
            if c == t:
                tn += 1
        
    Q = makeQueue(B)

    print('Possible' if isWinable(B, Q, t, tn) else 'Impossible')

    t = input()[0]
