from numpy import array
tn = array([str]*20)
tm = array([float()]*20)

# Saisie des données
ne = int(input("Nombre d'élèves ? "))
while ne < 4 or ne > 40:
    ne = int(input("Nombre d'élèves ? "))

for i in range(ne):
    print("Elève n°", i+1)

    tn[i] = input("Nom ? ")
    while tn[i] == "":
        tn[i] = input("Nom ? ")

    tm[i] = float(input("Moyenne ? "))
    while tm[i] < 0 or tm[i] > 20:
        tm[i] = float(input("Moyenne ? "))

# Calcul de la meilleure moyenne
mc = 0
for i in range(ne):
    mc = mc + tm[i]
mc = mc / ne
print("Moyenne de la classe : ", round(mc, 2))

# Affichage des meilleurs élèves
print("Les élèves qui ont obtenu du dessus de la moyenne sont :")
for i in range(ne):
    if tm[i] >= mc:
        print(tn[i], tm[i])

"""
8
Asma
17.5
Akram
18.5
Chiraz
19.5
Salim
18.5
Bassem
19.5
Salma
15.5
Dania
16.5
Youssef
17.25
"""