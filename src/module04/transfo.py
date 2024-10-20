u1 = int(input("Tension d'entrée ? "))
u2 = int(input("Tension de sortie ? "))
r21 = u2 / u1
if r21 > 1.03:
    print("Transformateur élévateur")
elif r21 < 0.97:
    print("Transformateur abaisseur")
else:
    print("Transformateur isolateur")