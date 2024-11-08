from random import randint
n = int(input("Donner n ? "))

seq = ""
for i in range(n):
    seq += chr(randint(65, 90))

print(seq)

car = input("Lettre à chercher ? ")
nb = 0
for i in range(n):
    if seq[i] == car:
        nb += 1

print("Le", car, "est trouvé", nb, "fois")

