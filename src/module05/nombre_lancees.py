from random import randint

nb =  int(input("Un nombre [1, 6] ? "))
nbl = 0
valide = False
while not valide:
    nbl = nbl + 1
    de = randint(1, 6)
    print("Lancée", nbl, ":", de)
    valide = de == nb
print("Nombre de lancées :", nbl)