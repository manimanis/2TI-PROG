from random import randint

n = 10
t = [-2, -10, 2, 3, 8, -6, -3, 10, -1, -5]
t2 = [int() for _ in range(n)]
print(t)

d = 0
f = n-1
for i in range(n):
    if t[i] < 0:
        t2[d] = -t[i]
        d += 1
    else:
        t2[f] =  2 * t[i]
        f -= 1
print(t2)
for i in range(d):
    print(t2[i], end=", ")
print()
for i in range(n-1, d-1, -1):
    print(t2[i], end=", ")