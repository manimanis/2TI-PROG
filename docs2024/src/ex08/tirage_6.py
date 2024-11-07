from random import randint
nb6 = 0
for i in range(100):
    n = randint(1, 6)
    if n == 6:
        nb6 += 1
print("Apparitions 6 :", nb6)
