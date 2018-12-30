import math

def prob(sigma, a, b):
    s = 2 * (sigma ** 2)
    return (math.exp(- (a ** 2)/s) - math.exp(- (b ** 2)/s))

line = input().split()
s = float(input())
rad = [0]
points = [50, 25, 10.5, 31.5, 10.5, 21]

for i in range(len(line)):
    rad.append(float(line[i]))

e = 0

for i in range(len(rad)-1):
    e += points[i] * prob(s, rad[i], rad[i+1])

print(e)
