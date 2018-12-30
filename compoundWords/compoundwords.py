import sys
cwords = set()
words = []

for l in sys.stdin:
    line = l.split()
    for w in line:
        words.append(w)

for i, w in enumerate(words):
    for j, v in enumerate(words):
        if i != j:
            cw = w + v
            cwords.add(cw)

for w in sorted(cwords):
    print(w)
