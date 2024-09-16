from numpy import array


def saisie():
    n = int(input("Nombre de colis [1, 30] ? "))
    while n < 1 or n > 30:
        n = int(input("Nombre de colis [1, 30] ? "))
    return n


def valide(ch):
    v = len(ch) == 6 and "UPN".find(ch[0]) != -1
    i = 1
    while v and i < len(ch):
        v = "0" <= ch[i] <= "9"
        i += 1
    return v


def remplir(n):
    t = array([str]*n)
    for i in range(n):
        t[i] = input(f"Ref. colis n°{i} ? ")
        while not valide(t[i]):
            t[i] = input(f"Ref. colis n°{i} ? ")
    return t


def classer(n, t, pri):
    t1 = array([str]*n)
    n1 = 0
    for i in range(n):
        if t[i][0] == pri:
            t1[n1] = t[i]
            n1 += 1
    return n1, t1

def afficher(n, t):
    for i in range(n):
        print(t[i], end=' ; ')
    print()

# PP
n = saisie()
t = remplir(n)

nu, tu = classer(n, t, "U")
print("Colis urgents")
afficher(nu, tu)

np, tp = classer(n, t, "P")
print("Colis priortaires")
afficher(np, tp)

nn, tn = classer(n, t, "N")
print("Colis normaux")
afficher(nn, tn)
