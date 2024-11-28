from random import randint
n = 8
print(f"Nombre d'obstacles (2 ≤ n ≤ 10) ? {n}")
for i in range(n):
    num = i+1
    angle = randint(-150, 150)
    dist = randint(15, 100)
    print(f"Mesure n°{num} ? obs{num},{angle},{dist}")