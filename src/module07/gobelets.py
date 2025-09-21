def Switch(x, y):
    aux = x
    x = y
    y = aux
    return x, y 


def Exchange(x, y):
    aux = x
    x = y
    y = aux

Goblet = [False, True, False]

n = int(input("Nombre de permutations ? "))

for i in range(n):
    Goblet[0], Goblet[1] = Switch(Goblet[0], Goblet[1])
    Exchange(Goblet[1], Goblet[2])
    Goblet[2], Goblet[0] = Switch(Goblet[2], Goblet[0])

for i in range(3):
    if Goblet[i]:
        print("Balle sous le gobelet", chr(65+i))
