from random import randint

n = 10
x = [randint(1, 100) for _ in range(n)]

v = randint(1, 100)

vpp = x[0]
for i in range(1, n):
    if abs(x[i]-v) < abs(vpp - v):
        vpp = x[i]

print(v, x, vpp)