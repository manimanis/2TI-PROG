from random import randint, seed
from numpy import array

# seq 1
n = int(input("Nombre pair [2, 20] ? "))
while n < 2 or n > 20 or n % 2 != 0:
    n = int(input("Nombre pair [2, 20] ? "))
# seq 2
seed(n)
t = array([int()]*20)
t1 = array([int()]*20)
for i in range(n):
    t[i] = randint(1, 30)
# seq 3
print("t:", end=" ")
for i in range(n):
    print(t[i], end=" ")
print()
# seq 4
n1 = 0
for i in range(n-1):
    if t[i] > t[n-1]:
        t1[n1] = t[i]
        n1 = n1 + 1
#seq 5
print("t:", end=" ")
for i in range(n1):
    print(t1[i], end=" ")
print()
