long = float(input("Longueur (m) ? "))
larg = float(input("Largeur (m) ? "))
cote = int(input("Carrelage (cm) ? "))

longcm = int(long * 100)
largcm = int(larg * 100)

nblong = longcm // cote + (longcm % cote >= 5)
nblarg = largcm // cote + (largcm % cote >= 5)

nbp = nblong * nblarg

print("La pièce nécessite", nbp, "carreaux.")