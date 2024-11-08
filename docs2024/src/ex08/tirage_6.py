from random import randint
n = int(input("Donner n ? "))
nb6 = 0
for i in range(100):
    v = randint(1, 6)
    if v == 6:
        nb6 += 1
perc = (nb6 * 100) // n
print("Apparitions 6 :", nb6)
print("Pourcentage :", perc, "%")
