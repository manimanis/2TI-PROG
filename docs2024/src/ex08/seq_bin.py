from random import randint
n = int(input("Donner n ? "))

seq = ""
nb0 = 0
nb1 = 0
for i in range(n):
    v = randint(0, 1)
    seq += str(v)
    nb0 += (v == 0)
    nb1 += (v == 1)
print("Séq :", seq)
print("Nb 0 :", nb0)
print("Nb 1 :", nb1)

