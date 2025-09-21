from math import floor


notes = [int(v) for v in """2
5
5
7
4
5
5
5
4
4""".split()]
note_tot = 11.5
total = sum(notes)
npq = note_tot / total
print(f"{npq} x {total} = {note_tot}")
valeurs = [float()] * len(notes)
somme = 0
for idx, note in enumerate(notes):
    valeur = floor(npq * note / 0.25) * 0.25
    valeurs[idx] = valeur
    somme += valeur
for idx, note in enumerate(notes):
    valeur = npq * note
    if somme < note_tot and valeur > valeurs[idx]:
        print(idx)
        valeurs[idx] += 0.25
        somme += 0.25
for valeur in valeurs:
    print(valeur)
