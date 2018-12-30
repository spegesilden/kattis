import sys
import math

def sunday(M, P, L, E, R, S, EGGS):
    m = math.floor(P/S)
    p = math.floor(L/R)
    eggs = M * E

    return [m, p, EGGS, eggs]

def mosquitos(M, P, L, E, R, S, N):
    m = [M, P, L, 0]

    for i in range(N):
        m = sunday(m[0], m[1], m[2], E, R, S, m[3])
        print(i+1, m)

    return m[0]

for line in sys.stdin:
    l = line.split()

    if int(l[4]) == 0 or int(l[5]) == 0:
        print(0)
    else:
        print(mosquitos(int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5]), int(l[6])))
