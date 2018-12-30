import math

def genSylvester(H):
    n = len(H)
    S = [H[i % n][:] for i in range(2*n)]

    for i in range(len(S)):
        for j in range(n):
            E = H[i % n][j]
            if i >= n:
                E *= -1
            S[i].append(E)

    return S

def append(H, S):
    for h in H:
        S.append(h)

def merge(A, B):
    for i in range(len(A)):
        for b in B[i]:
            A[i].append(b)

def minus(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] *= -1
    return A

def getSub(n, x, y, w, h):
    if n == 1:
        return [[1]]

    sub = []
    subR = []
    m = int(n/2)
    print(m,n,x,y,w,h)

    if x + w <= m + 1 and y + h <= m + 1:
        print('First')
        append(getSub(m, x, y, w, h), sub)
    elif x + w <= m + 1 and y + h > m + 1:
        print('Second')
        if y <= m + 1:
            append(getSub(m, x, y, w, h + y - m), sub)
            append(getSub(m, x, 1, w, m - y), sub)
        else:
            append(getSub(m, x, y % m, w, h), sub)
    elif x + w > m + 1 and y + h <= m + 1:
        print('Third')
        if x <= m + 1:
            append(getSub(m, x, y, w + x - m, h), sub)
            append(getSub(m, 1, y, m - x, h), subR)
            merge(sub, subR)
        else:
            append(getSub(m, x % m, y, w, h), sub)
    else:
        print('Forth')
        if x <= m + 1 and y <= m + 1:
            append(getSub(m, x, y, w + x - m, h + y - m), sub)
            append(getSub(m, x, 1, w + x - m, m - y), sub)
            append(getSub(m, 1, y, m - x, h + y - m), subR)
            append(minus(getSub(m, 1, 1, m - x, m - y)), subR)
            merge(sub, subR)
        elif x <= m + 1 and y > m + 1:
            append(getSub(m, x, y % m, w + x - m, h), sub)
            append(minus(getSub(m, 1, y % m, m - x, h)), subR)
            merge(sub, subR)
        elif x > m + 1 and y <= m + 1:
            append(getSub(m, x, y, w, h + y - m), sub)
            append(minus(getSub(m, x, 1, w, m - y)), subR)
            merge(sub,subR)
        else:
            append(minus(getSub(m, x % m, y % m, w, h)), sub)

    return sub

Syl = [[[1]]]

N = int(input())

for j in range(N):
    line = input().split()
    n = int(line[0])
    x = int(line[1]) + 1
    y = int(line[2]) + 1
    w = int(line[3])
    h = int(line[4])
    m = len(Syl)

    sub = getSub(n, x, y, w, h)

    for i in range(len(sub)):
        s = str(sub[i][0])
        for j in range(1, len(sub[i])):
            s += ' ' + str(sub[i][j])
        print(s)
