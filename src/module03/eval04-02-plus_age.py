chage = input("Âges des personnes séparés par des virgules ? ")

p1 = chage.find(",") # Position 1ère virgule
# Enlever la partie qui précède la 1ère virgule
chage1 = chage[p1+1:]
p2 = chage1.find(",") # Position 2ème virgule

a1 = int(chage[0:p1])   # âge 1ère personne
a2 = int(chage1[0:p2])  # âge 2ème personne
a3 = int(chage1[p2+1:]) # âge 3ème personne

if a1 >= a2 and a1 >= a3:
    print("1ère Personne plus âgée")
if a2 >= a1 and a2 >= a3:
    print("2ème Personne plus âgée")
if a3 >= a1 and a3 >= a2:
    print("3ème Personne plus âgée")
