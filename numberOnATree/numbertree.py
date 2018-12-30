line = input().split()
h = int(line[0])
node = (2 ** (h + 1)) - 1

if len(line) == 1:
    print(node)
else:
    path = line[1]
    r = 0
    n = 0

    for i, s in enumerate(path):
        if s == 'R':
            r += 2 ** (len(path) - i - 1)

    for i in range(len(path), h + 1):
        n += 2 ** i

    print(n - r)
