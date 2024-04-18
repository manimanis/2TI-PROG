from numpy import array

def saisie():
    n = int(input("N [10, 10000] ? "))
    while n < 10 or n > 10000:
        n = int(input("N [10, 10000] ? "))
    return n

def facteurs(n):
    t = array([int()]*7)
    f = 2
    idx = 0
    while n >= f:
        if n % f == 0:
            t[idx] = f
            idx += 1
            while n % f == 0:
                n //= f
        else:
            f += 1
    return t, idx

n1 = saisie()
n2 = saisie()

t1, nf1 = facteurs(n1)
t2, nf2 = facteurs(n2)

if nf1 == nf2:
    print(n1, "et", n2, "ont le même nombre de facteurs premiers.")
else:
    print(n1, "et", n2, "n'ont pas le même nombre de facteurs premiers.")

