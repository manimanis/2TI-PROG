from random import randint
x = randint(1, 5)
y = randint(1, 5)
print(x, y)
print("Position de tir")
col = int(input("Colonne ? "))
lig = int(input("Ligne ? "))
print("Position bateau : ", x, ", ", y)
if col == x and lig == y:
    print("Touché")
elif col == x or lig == y:
    print("En vue")
else:
    print("A l'eau")