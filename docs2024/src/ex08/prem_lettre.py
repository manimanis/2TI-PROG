ph = input("Donner une phrase ? ")
for i in range(len(ph)):
    if i == 0 or ph[i - 1] == ' ' and ph[i] != ' ':
        print(ph[i].upper(), end="")
# La confiance en soi est le premier secret du succès.