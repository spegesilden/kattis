def toRevBinary(n):
    s = ''
    while n > 0:
        if n % 2 == 1:
            s += '1'
            n = int((n - 1)/2)
        else:
            s += '0'
            n = int(n/2)
    return s

def toDecimal(s):
    n = 0
    for i, c in enumerate(s):
        if c == '1':
            exponent = len(s) - i - 1
            n += 2 ** exponent
    return n

n = int(input())
s = toRevBinary(n)
print(toDecimal(s))
