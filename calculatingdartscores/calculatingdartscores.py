P = [20 - i for i in range(20)]
P2 = [2*i for i in P]
P3 = [3*i for i in P]

def divide(n, i):
    m = i

    while m <= n:
        m += i

    return m - i
    

def isScore(n):
    if n <= 20:
        return [n]

    C = []
    m = 0

    for j in range(3):
        for i in P:
            


