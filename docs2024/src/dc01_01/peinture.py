cd = input("Couleur désirée ? ")
cd2 = cd[:2].upper()
couleurs = ""
if cd2 == "CY" or cd2 == "VE" or cd2 == "VI" or cd2 == "NO":
    couleurs += "Cyan + "
if cd2 == "MA" or cd2 == "OR" or cd2 == "VI" or cd2 == "NO":
    couleurs += "Magenta + "
if cd2 == "JA" or cd2 == "OR" or cd2 == "VE" or cd2 == "NO":
    couleurs += "Jaune + "
if couleurs == "":
    print("Couleur inconnue!")
else:
    print(cd, "=", couleurs[:-3])
