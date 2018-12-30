n = int(input())

while n > -1:
    m = 0
    t = []
    s = []

    for i in range(n):
        line = input().split()
        s.append(int(line[0]))
        t.append(int(line[1]))

    for i in range(n):
        time = 0
        if i == 0:
            time = t[0]
        else:
            time = t[i] - t[i-1]
        m += s[i] * time

    print(str(m) + ' miles')

    n = int(input())
