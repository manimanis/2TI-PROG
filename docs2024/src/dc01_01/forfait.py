numc = input("Numéro téléphone ? ")
numt = input("Numéro ticket ? ")

if len(numc) != 8 or not numc.isdecimal():
    print("Numéro téléphone invalide.")
elif len(numt) < 14 or not numt.isdecimal():
    print("Numéro de ticket incorrect.")
elif numt.find(numc) != -1:
    print("Forfait 5Go gagné!")
elif numt.find(numc[:3]) != -1:
    print("Forfait 1Go gagné!")
elif numt.find(numc[:2]) != -1:
    print("Forfait 300Mo gagné!")
else:
    print("Merci pour votre fidélité.")

"""
# cas 1
22248453
22248453022592
-> 5Go

# cas 2
22581364
22248453022592
-> 1Go

# cas 3
24581364
22248453022592
-> 330Mo

# cas 4
29581364
22248453022592
-> Merci pour votre fidélité.

# cas 5
23459687
22248453
"""