n = int(input())

for i in range(n):
    x = input()
    print(x + ' is even' if int(x) % 2 == 0 else x + ' is odd')
