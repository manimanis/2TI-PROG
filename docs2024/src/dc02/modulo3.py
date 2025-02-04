from random import randint


i = 1
j = 3
while i < 50:
    print(i, end=", ")
    i += j
    j = (j - 1) % 4
print()

t = [randint(100, 999) for _ in range(8)]
print(t)


t = [randint(0, 99) for _ in range(20)]
print(t)
