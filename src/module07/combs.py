def saisie(a, b):
    n = int(input("Donner un entier ["+str(a)+", "+str(b)+"] ? "))
    while n < a or n > b:
        n = int(input("Donner un entier ["+str(a)+", "+str(b)+"] ? "))
    return n


def fact(n):
    fn = 1
    for i in range(2, n + 1):
        fn = fn * i
    return fn


def comb(n, p):
    return fact(n) // (fact(p) * fact(n - p))


# Programme principal
n = saisie(1, 20)
p = saisie(0, n)

cnp = comb(n, p)

print(f"Le nombre de combinaisons possibles est : {cnp}")
