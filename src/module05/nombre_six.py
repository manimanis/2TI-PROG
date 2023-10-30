from random import randint


nb6 = 0
for i in range(10):
    de = randint(1, 6)
    print("Lancée", i, ":", de)
    if de == 6:
        nb6 = nb6 + 1
print("Nombre de 6 :", nb6)