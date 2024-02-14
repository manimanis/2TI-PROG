from numpy import array
from random import randint

no = int(input("Nombre d'oranges ? "))
while no < 10 or no > 100000:
    no = int(input("Nombre d'oranges ? "))

td = array([int()]*no)
for i in range(no):
    p = randint(0, 1000)
    if p < 5:
        td[i] = randint(30, 52)
    elif p < 750:    
        td[i] = randint(53, 72)
    elif p < 950:
        td[i] = randint(73, 92)
    else:
        td[i] = randint(93, 110)

nca, ncb, nccd = 0, 0, 0
toca = array([int()]*no)

for i in range(no):
    if td[i] < 73:
        nccd += 1
    elif td[i] < 93:
        ncb += 1
    else:
        toca[nca] = td[i]
        nca += 1

print("Nombre d'oranges")
print("Calibre a :", nca)
print("Calibre b :", ncb)
print("Calibre c+d :", nccd)

opp, opg = toca[0], toca[0]
for i in range(nca):
    if toca[i] > opg:
        opg = toca[i]
    if toca[i] < opp:
        opp = toca[i]
print("Fruit le plus petit", opp, "mm")
print("Fruit le plus grand", opg, "mm")


