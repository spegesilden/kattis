def isSeq(seq):
    r = seq[0] - seq[1]

    for i in range(1, len(seq)-1):
        if seq[i] - seq[i+1] != r:
            return False

    return True

n = int(input())

for i in range(n):
    l = input().split()
    seq = []

    for i in range(1, len(l)):
        seq.append(int(l[i]))

    if isSeq(seq):
        print('arithmetic')
    elif isSeq(sorted(seq)):
        print('permuted arithmetic')
    else:
        print('non-arithmetic')
