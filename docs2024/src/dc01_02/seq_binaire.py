from random import randint
ls = int(input("Longueur séquence ? "))
ns = int(input("Nbre de séquences ? "))

seuil = 0
nbt1 = 0
for i in range(ns):
    seuil += 5
    ch = ""
    nb1 = 0
    for j in range(ls):            
        v = randint(0, 100)
        if v <= seuil:
            ch = ch + "1"
            nb1 += 1
            nbt1 += 1
        else:
            ch = ch + "0"
    print(ch, nb1)
densite = nbt1 * 100 / ls /ns
print("Total :", nbt1)
print("Densité :", densite, '%')
