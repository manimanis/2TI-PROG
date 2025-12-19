
import random

# Séquence 1
n = int(input("n ? "))
p = int(input("p ? "))

# Séquence 2
ch1 = ""
for i in range(1, n + 1):
    ch1 += str(i // 10) + str(i % 10)

# Séquence 3
ch2 = ""
for i in range(1, p + 1):
    p1 = (random.randint(0, len(ch1) - 1) // 2) * 2
    ch2 += ch1[p1:p1 + 2]
    ch1 = ch1[:p1] + ch1[p1 + 2:]

# Séquence 4
for i in range(0, len(ch2), 2):
    v = int(ch2[i:i + 2])
    print(v)
