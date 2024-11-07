n = int(input("Donner n ? "))
s = 0
for i in range(0, n + 1, 3):
    if i % 2 != 0:
        s += i
print("Somme =", s)