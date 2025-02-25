from random import randint


def saisir():
    while True:
        n = int(input("Nbre employés ? "))
        if 3 <= n <= 20:
            break
    return n


def verif_nom(ch):
    return len(ch) < 7 or ch.find(" ") > 0


def produit_chiff(n):
    p = 1
    while n != 0:
        r = n % 10
        n //= 10
        if r != 0:
            p *= r
    return p

def lettre_alea(n):
    ch = ""
    for i in range(n):
        c = randint(0, 1)
        if c == 0:
            ch += chr(randint(65, 90))
        else:
            ch += chr(randint(97, 122))
    return ch

def remplir_emp(tu, ta, n):
    for i in range(n):
        print(f"Utilisateur {i+1}")
        while True:
            tu[i] = input("Nom ? ")
            if verif_nom(tu[i]):
                break
        while True:
            ta[i] = int(input("Année d'embauche ? "))
            if 2000 <= ta[i] <= 2025:
                break

def generer(tu, ta, tm, n):
    for i in range(n):
        tm[i] = tu[i][:tu[i].find(' ')] + str(produit_chiff(ta[i])) + lettre_alea(3) + str(randint(100, 999))
    print(tm[:n])

#
tu = [""] * 20
ta = [int()] * 20
tm = [""] * 20

n = saisir()
remplir_emp(tu, ta, n)
generer(tu, ta, tm, n)

"""
7
Salim Fekih
2010
Baya Ayoub
2025
Kamel Faleh
2024
Youssef Amer
2008
Mourad Béji
2013
Nour Ayeb
2005
Ridha Hassen
2018
"""


