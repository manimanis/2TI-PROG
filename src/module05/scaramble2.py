
from random import randint

msg1 = input("Votre message ? ")

alp = ""
for i in range(26):
    alp += chr(65 + i)

ch2 = alp
clé = ""
for i in range(26):
    p1 = randint(0, len(ch2) - 1)
    clé += ch2[p1]
    ch2 = ch2[:p1] + ch2[p1 + 1:]

msg2 = ""
for i in range(len(msg1)):
    car = msg1[i]
    if "A" <= car.upper() <= "Z":
        r = ord(car.upper()) - 65
        car = clé[r]
    msg2 += car

print(alp)
print(clé)
print(msg1)
print(msg2)
