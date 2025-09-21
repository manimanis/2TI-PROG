from numpy import array

n = int(input("Taille du tableau ? "))

nb = array([int()]*3)
t = array([int()]*n)

for i in range(n):
    t[i] = int(input(f"t[{i}] ? "))

for i in range(n):
    nb[i % 3] = nb[i % 3] + t[i]

print(nb)