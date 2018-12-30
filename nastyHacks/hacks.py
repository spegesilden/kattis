n = int(input())

for i in range(n):
    line = input().split()
    r = int(line[0])
    e = int(line[1])
    c = int(line[2])

    if r < e - c:
        print('advertise')
    elif r > e - c:
        print('do not advertise')
    else:
        print('does not matter')
