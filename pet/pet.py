player = 0
points = 0

for i in range(5):
    line = input().split()
    p = 0

    for s in line:
        p += int(s)

    if p > points:
        points = p
        player = i + 1

print(player, points)
