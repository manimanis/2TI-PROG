from random import randint
from numpy import array

vp = array([int()]*8)
np = array([int()]*8)

for i in range(8):
    vp[i] = int(input(f"Monnaie dans tiroir n°{i} ? "))
    while vp[i] not in [5000, 2000, 1000, 500, 200, 100]:
        vp[i] = int(input(f"Monnaie dans tiroir n°{i} ? "))
    np[i] = int(input(f"Nb. pièces dans tiroir n°{i} ? "))
    while np[i] < 0 or np[i] > 200:
        np[i] = int(input(f"Nb. pièces dans tiroir n°{i} ? "))

pb = int(input("Prix d'une boisson ? "))
while pb % 100 != 0 or pb < 1000 or pb > 10000:
    pb = int(input("Prix d'une boisson ? "))

mt = int(input("Montant introduit ? "))
while mt < pb and mt % 500 != 0:
    mt = int(input("Montant introduit ? "))

mar = mt - pb
print(f"Montant à rendre = {mar}")

i = 0
rendu = ""
while mar > 0 and i < 8:
    if mar >= vp[i] and np[i] > 0:
        if rendu != "":
            rendu += "+"
        rendu += str(vp[i])
        mar -= vp[i]
        np[i] -= 1
    else:
        i += 1
print(f"Pieces rendues = {rendu}")

ca = 0
for i in range(8):
    ca += vp[i] * (np[i] - 20)
print(f"Chiffre d'affaires = {ca}")

"""
Test 1
------
5000
38
2000
11
1000
30
500
28
200
1
200
20
100
4
100
20
2800
5000

Test 2
------
5000
72
2000
3
1000
33
500
27
200
0
200
0
100
0
100
0
3300
4000
"""