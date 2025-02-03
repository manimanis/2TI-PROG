from random import randint


vp = [5000, 2000, 1000, 500, 200, 200, 100, 100]
np = [20 for _ in vp]

ca1 = 0
n = 3 # randint(20, 100)
for _ in range(n):
    prix = round(randint(19, 30) * 100, 3)
    pieces = []
    total = 0
    while total < prix:
        piece = vp[randint(0, 3)]
        total += piece
        pieces.append(piece)
    ca1 += prix
    rendu = total - prix
    print(prix, total, pieces, rendu)
    for piece in pieces:
        idx = vp.index(piece)
        np[idx] += 1
    i = 0
    while rendu > 0 and i < len(vp):
        if rendu >= vp[i] and np[i] > 0:
            np[i] -= 1
            rendu -= vp[i]
        else:
            i += 1
    print(rendu, np)

ca = 0
for v, n in zip(vp, np):
    ca += v * (n - 20)
print(ca, ca1)
