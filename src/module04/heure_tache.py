h = input("Heure début (hh:mm) ? ")
d = int(input("Durée (minutes) ? "))

hh = int(h[:2])
mm = int(h[3:])

if hh > 23 or hh < 0 or mm > 59 or mm < 0 or d <= 0:
    print("Données incorrectes")
    exit()

mm2 = mm + d
hh2 = hh + mm2 // 60
mm2 = mm2 % 60
jj2 = hh2 // 24
hh2 = hh2 % 24

if jj2 > 0:
    print(f"La tâche prend fin à {hh2:02}:{mm2:02}, {jj2} jour(s) après")
else:
    print(f"La tâche prend fin à {hh2:02}:{mm2:02}")