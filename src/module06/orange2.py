from numpy import array
from random import randint

no = int(input("Nombre d'oranges ? "))
while no < 10 or no > 100000:
    no = int(input("Nombre d'oranges ? "))

td = array([int()]*no)
for i in range(no):
    p = randint(0, 1000)
    if p < 5:
        td[i] = randint(30, 52)
    elif p < 750:    
        td[i] = randint(53, 72)
    elif p < 950:
        td[i] = randint(73, 92)
    else:
        td[i] = randint(93, 110)

dm = int(input("Diamètre minimal ? "))
while dm < 30 or dm > 110:
    dm = int(input("Diamètre minimal ? "))

if dm < 53:
    cl = "D"
elif dm < 73:
    cl = "C"
elif dm < 93:
    cl = "B"
else:
    cl = "A"
print(f"Le ø {dm} correspond à la classe {cl}")

ndm = 0
for i in range(no):
    if td[i] >= dm:
        ndm += 1

print(f"{ndm}/{no} oranges ont un ø >= {dm}")
