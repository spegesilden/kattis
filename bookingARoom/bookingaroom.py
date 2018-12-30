line = input().split()
r = int(line[0])
n = int(line[1])
rooms = {i+1 for i in range(r)}

for i in range(n):
    rooms.remove(int(input()))

if len(rooms) == 0:
    print ('too late')
else:
    print(rooms.pop())
