from numpy import array
from random import randint

n = int(input("Nbre équipes ? "))
while n <= 0 or n > 20:
    n = int(input("Nbre équipes ? "))

teq = array([str]*20)
tnbp = array([int()]*20)
for i in range(n):
    teq[i] = input("Equipe ? ")
    tnbp[i] = int(input("Pts ? "))
    while i != 0 and tnbp[i] > tnbp[i-1]:
        tnbp[i] = int(input("Pts ? "))

rang = 1
for i in range(n):
    if i > 0 and tnbp[i] != tnbp[i-1]:
            rang = i+1
    print(rang, teq[i], tnbp[i])

"""
7
ESS
13
OB
12
CA
12
ST
8
USBG
7
EGSG
6
ASS
0
"""
