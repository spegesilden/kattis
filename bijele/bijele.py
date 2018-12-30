pieces = input().split()
piecesNeeded = [1,1,2,2,2,8]
piecesMissing = []

for i,p in enumerate(pieces):
    piecesMissing.append(piecesNeeded[i]-int(p))
print(*piecesMissing)
