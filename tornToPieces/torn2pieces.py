n = int(input())
connections = {}

for i in range(n):
    l = input().split()
    connections[l[0]] = set(l[1::])
    for s in l[1::]:
        if s not in connections.keys():
            connections[s] = set([l[0]])
        else:
            connections[s].add(l[0])

endStations = input().split()

def isRouteable(route, h):
    notSeen = h.copy()
    if route[-1] in notSeen:
        notSeen.remove(route[-1])
    else:
        return False

    if route[-1] == endStations[1]:
        return route

    routeable = False

    for s in connections[route[-1]]:
        if s in h:
            newRoute = route[::]
            newRoute.append(s)
            routeable = routeable or isRouteable(newRoute, notSeen)

    return routeable

h = set([])

for s in connections.keys():
    h.add(s)

route = isRouteable([endStations[0]], h)

if route:
    s = route[0]
    for i in range(1, len(route)):
        s += ' ' + route[i]
    print(s)
else:
    print('no route found')
