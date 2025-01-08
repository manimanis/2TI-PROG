from random import randint
from numpy import array


n = int(input("Donner n ? "))
while (n < 3) or (n > 15) or (n % 2 != 1):
    n = int(input("Donner n ? "))

t = array([int()]*n)
tp = array([int()]*n)
# Partie 2
for i in range(n):
    t[i] = randint(1, 99)
    print(t[i], end="\t")
print()

# Partie 3
np = 0
for i in range(n):
    if t[i] % 2 == 0:
        tp[np] = t[i]
        np = np + 1

# Partie 4
for i in range(np):
    print(tp[i], end="\t")
print()