from numpy import array
from random import randint

nf = int(input("Nombre d'oranges ? "))
while nf < 10 and nf > 200000:
    nf = int(input("Nombre d'oranges ? "))

ttai = array([int()]*nf)
for i in range(nf):
    p = randint(0, 1000)
    if p < 5:
        ttai[i] = randint(30, 52)
    elif p < 750:    
        ttai[i] = randint(53, 72)
    elif p < 950:
        ttai[i] = randint(73, 92)
    else:
        ttai[i] = randint(93, 110)

nca, ncb, nccd = 0, 0, 0
tcla = array([int()]*nf)

for i in range(nf):
    if ttai[i] < 73:
        nccd += 1
    elif ttai[i] < 93:
        ncb += 1
    else:
        tcla[nca] = ttai[i]
        nca += 1

print("Nombre de fruits")
print("Calibre a :", nca)
print("Calibre b :", ncb)
print("Calibre c+d :", nccd)

fpp, fpg = tcla[0], tcla[0]
for i in range(nca):
    if tcla[i] > fpg:
        fpg = tcla[i]
    if tcla[i] < fpp:
        fpp = tcla[i]
print("Fruit le plus petit ", fpp, "mm")
print("Fruit le plus grand ", fpg, "mm")


