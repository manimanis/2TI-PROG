from random import randint

n = 3
x = [int(v) for v in input(f"Entrer {n} entier ? ").split()]

v = int(input("Entrer v ? "))

vpp = x[0]
for i in range(1, n):
    if abs(x[i]-v) < abs(vpp - v):
        vpp = x[i]

print(v, x, vpp)