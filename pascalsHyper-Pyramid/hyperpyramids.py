line = input().split()
d = int(line[0])
h = int(line[1])

def makePlane(l):
    plane = []

    for i in range(d):
        p = [0 for i in range(d)]
        for j in range(l):
            p[i] = j



pyramid  = {[0 for i in range(d)]: 1}

#for i in range(h):
