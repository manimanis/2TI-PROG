ph = input("Donner une phrase ? ")
cons = 0
voy = 0
for i in range(len(ph)):
    car = ph[i].upper()
    if "A" <= car <= "Z":
        if car in ["O","I", "Y","E","A","U"]:
            voy += 1
        else:
            cons += 1
print("Consonnes =", cons)
print("Voyelles =", voy)
# La confiance est le ciment invisible qui conduit une équipe à l'excellence et une relation à la profondeur.