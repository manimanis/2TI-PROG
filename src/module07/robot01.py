from numpy import array


def verif_pos(p):
    return (len(p) == 3 and
            '0' <= p[0] <= '9' and
            p[1] == ',' and
            '0' <= p[2] <= '7' and
            p != '0,0' and
            p != '9,7')


def saisie_pos(n):
    p = input(f"Position de l'objet n°{n} ? ")
    while not verif_pos(p):
        p = input(f"Position de l'objet n°{n} ? ")
    return p


def existe(obj, n, t):
    i = 0
    tr = False
    while not tr and i < n:
        tr = obj == t[i]
        i += 1
    return tr


def remplir():
    n = int(input("Nombre d'objets [1, 49] ? "))
    while n < 1 or n > 49:
        n = int(input("Nombre d'objets [1, 49] ? "))

    t = array([str]*n)
    for i in range(n):
        t[i] = saisie_pos(i+1)
        while existe(t[i], i, t):
            t[i] = saisie_pos(i+1)
    return n, t


def dist(p):
    x = int(p[0])
    y = int(p[2])
    return x*x+y*y


def plus_proche(n, t):
    pp = 0
    for i in range(1, n):
        if dist(t[pp]) > dist(t[i]):
            pp = i
    return pp


def deplacer(n, t):
    t1 = array([str]*n)
    for i in range(n):
        pp = plus_proche(n, t)
        t1[i] = 'O' + str(pp+1) + ':' + t[pp]
        t[pp] = '9,7'
    return t1


def afficher(n, t):
    for i in range(n):
        print(t[i], end=' ; ')
    print()


# PP
n, t = remplir()
t1 = deplacer(n, t)
afficher(n, t1)
