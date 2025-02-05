from random import randint


i = 1
j = 3
while i <= 30:
    print(i, end=", ")
    i += j
    j = (j - 1) % 4
print()

t = [randint(100, 999) for _ in range(8)]
print(t)


t = [randint(0, 99) for _ in range(20)]
print(t)

#ex1
i = 0
for j in range(1, 5):
    for k in range(3):        
        i += j
        print(i, end=", ")
print()
i = 0
j = 1
while j <= 4:
    k = 1
    while k <= 3:
        i += j
        print(i, end=", ")
        k += 1
    j += 1
print()
 
t1 = [552, 277, 585, 258]
t2 = [0 for _ in range(10)]
for i in range(4):
    ch = str(t1[i])
    for j in range(len(ch)):
        p = int(ch[j])
        t2[p] += 1
for i in range(10):
    if t2[i] > 0:
        print(i, "-", t2[i])

t1 = [randint(0, 20) * 0.25 for _ in range(10)]
print(t1)

t1 = [15,11,81,8,82,69,90,63,22,40,80,13,75,50,70,25,21,2,21,79]
for t1i in t1:
    if 65 <= t1i <= 90:
        print(chr(t1i).lower(), end=", ")
