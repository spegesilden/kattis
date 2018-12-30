dom = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
notDom = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}

line = input().split()
n = int(line[0])
b = line[1]
maxSum = 0

for i in range(n):
    for j in range(4):
        h = input()
        if h[1] == b:
            maxSum += dom[h[0]]
        else:
            maxSum += notDom[h[0]]

print(maxSum)
