from numpy import array

# seq 1
n = int(input("N [10, 10000] ? "))
while n < 10 or n > 10000:
    n = int(input("N [10, 10000] ? "))

# seq 2
t = array([int()]*7)
n1 = n
f = 2
nf = 0
while n1 >= f:
    if n1 % f == 0:
        t[nf] = f
        nf += 1
        while n1 % f == 0:
            n1 //= f
    else:
        f += 1
# seq 3
for i in range(nf):
    print(t[i])