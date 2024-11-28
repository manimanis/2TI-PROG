n = int(input("Nombre d'obstacles (2 ≤ n ≤ 10) ? "))
dist_moy = 0
dist_min = 0
nom_min = ""
angle_min = ""
for i in range(n):
    mesure = input(f"Mesure n°{i+1} ? ")
    p1 = mesure.find(",")
    nom = mesure[:p1]
    p2 = mesure.find(",", p1+1)
    angle = int(mesure[p1+1:p2])
    dist = int(mesure[p2+1:])
    if dist_min == 0 or dist < dist_min:
        dist_min = dist
        nom_min = nom
        angle_min = angle
    dist_moy += dist
dist_moy = dist_moy // n
print(f"L'obstacle le plus proche est {nom_min}")
print(f"- Distance : {dist_min} cm")
print(f"- Angle : {angle_min} °")
print(f"Distance moyenne obstacles : {dist_moy} cm")