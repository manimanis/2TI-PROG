from random import randint
n = int(input("Donner n ? "))

seq = ""
for i in range(n):
    seq += chr(randint(65, 90))
print("Séq initiale :", seq)

seq1 = ""
for i in range(n):
    if seq1.find(seq[i]) == -1:
        seq1 += seq[i]
print("Séq finale   :", seq1)


