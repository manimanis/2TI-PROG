from numpy import array

# Saisie d'un paragraphe
par = input("Donner un paragraphe ? ")

# Initialisation du tableau
cpt = array([0]*26)

# Compter le nombre de lettres
for i in range(len(par)):
    if "A" <= par[i].upper() <= "Z":
      indice = ord(par[i].upper()) - ord("A")
      cpt[indice] = cpt[indice] + 1

# Afficher le nombre de lettres
dlc = 0
for i in range(26):
    if cpt[i] != 0:
        if dlc % 6 != 0:
            print(end=" - ")
        else:
            print()
        dlc = dlc + 1
        print(chr(65+i), ":", cpt[i], end="")
