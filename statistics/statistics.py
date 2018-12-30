import sys

index = 0

for l in sys.stdin:
    line = l.split()
    index += 1
    minimum = 10 ** 6
    maximum = - minimum

    for i in range(1, len(line)):
        n = int(line[i])
        if minimum > n:
            minimum = n
        if maximum < n:
            maximum = n

    print('Case ' + str(index) + ': ' + str(minimum) + ' ' + str(maximum) + ' ' + str(maximum - minimum))
