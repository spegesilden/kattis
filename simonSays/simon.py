t = int(input())

for i in range(t):
    line = input().split()
    if len(line) > 2:
        if line[0] == 'simon' and line[1] == 'says':
            s = line[2]
            for j in range(3, len(line)):
                s += ' ' + line[j]
            print(s)
        else:
            print('')
    else:
        print('')
