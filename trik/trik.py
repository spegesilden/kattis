perm = input()
positions = [1, 0, 0]

for p in perm:
    if p == 'A':
        tmp = positions[0]
        positions[0] = positions[1]
        positions[1] = tmp
    elif p == 'B':
        tmp = positions[1]
        positions[1] = positions[2]
        positions[2] = tmp
    else:
        tmp = positions[0]
        positions[0] = positions[2]
        positions[2] = tmp

for i in range(3):
    if positions[i] > 0:
        print(i + 1)
