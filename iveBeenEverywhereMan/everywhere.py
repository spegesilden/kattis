T = int(input())

for i in range(T):
    citySet = set()
    n = int(input())
    for j in range(n):
        citySet.add(input())
    print(len(citySet))
