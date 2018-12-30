n = int(input())
line = input().split()
A = []
pivots = []

for i in range(n):
    A.append(int(line[i]))

def partion(i, j):
    pivot = A[j]
    k = i - 1
    for m in range(i, j):
        if A[m] < pivot:
            k += 1
    if A[j] < A[k + 1]:

def pivots(i, j):
    if i < j:
        p = partition(i, j)
        pivots(i, p - 1)
        pivots(p + 1, j)

print(m)
