from math import exp, pi, sqrt
from random import randint, uniform

t = []
c1, c2, c3 = 0, 0, 0
n = 10000
for i in range(n):
    x = randint(0, 100)
    m = 0
    std = 30.0
    pomme = round(exp(-1/2*(x/std)**2)*(86.7-58.7)+58.7, 1)
    #print(pomme)
    if pomme < 67.9:
        c1 += 1
    elif pomme < 77.2:
        c2 += 1
    else:
        c3 += 1
print(c1/n, c2/n, c3/n)
# 58.7 - 67.0 - 81.4 - 86.7