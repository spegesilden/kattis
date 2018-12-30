import math

class Queue:
    def __init__(self, distance):
        self.q = []
        self.d = distance.copy()
        self.length = 0

    def pop(self):
        self.length -= 1
        return self.q.pop()

    def add(self, e):
        self.length += 1
        qNew = []

        if len(self.q) > 0:
            for node in self.q:
                if d[e] > d[node]:
                    qNew.append(e)
                qNew.append(node)
        else:
            qNew.append(e)

        self.q = qNew[::]

    def len(self):
        return self.length

    def contains(self, e):
        return e in self.q

isLine = True

while isLine:
    l = input().split()
    if len(l) < 2:
        isLine = False
    else:
        connections = {}
        n = int(l[1])
        for i in range(n):
            line = input().split()
            a = int(line[0])
            b = int(line[1])
            d = int(line[2])
            connections.setdefault(a, [[b, d]]).append([b, d])
            connections.setdefault(b, [[a, d]]).append([a, d])

        def routesBFS():
            q = []
            visited = set()

            q.append(1)
            result = 0

            while len(q) > 0:
                parent = q.pop()

                for child in connections[parent]:
                    if child == 2:
                        result += 1

                    if child in visited:
                        continue

                    if child not in q:
                        q.append(child)

                visited.add(parent)

            return result

        def routesDFS(r, ns):
            if r[-1] == 2:
                return 1

            notSeen = ns.copy()

            if r[-1] in ns:
                notSeen.remove(r[-1])

            result = 0

            for child in connections[r[-1]]:
                if child in notSeen:
                    route = r[::]
                    route.append(child)
                    result += routesDFS(route, notSeen)

            return result

        def routes():
            unvisited = set([])
            d = {}
            for node in connections.keys():
                unvisited.add(node)
                d[node] = math.inf
            d[1] = 0
            queue = Queue(d)
            queue.add(1)
            node = 1
            while queue.len() > 0 or not queue.contains(2):
                if node in unvisited:
                    unvisited.remove(node)
                    for child in connections[node]:
                        d[child[0]] = min(d[child[0]], d[node] + child[1])
                        queue.add(child[0])
                node = queue.pop()
            return d[2]

        ns = set([])
        for node in connections.keys():
            ns.add(node)

        print(routes())
