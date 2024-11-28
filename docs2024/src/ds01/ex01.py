from random import randint


ch = "Nour-Abdallah-Nourhène-Mehdi"
p1 = ch.find('-')
p2 = ch[p1+1:].find('-') + p1 + 1
p3 = ch[p2+1:].find('-') + p2 + 1
print(ch[p2+1:p3])
print(ch[p1+1:p3])

#-
a = 100
b = float(str(round(a / 6)) + '.' + str(a // 4))
print(b)

deb, fin = 120, 25
for i in range(deb, fin - 1, -(fin+2)):
    print(i, deb - 2 * i)

sgn = 1
s = 100
for i in range(1, 6):
    s += i * sgn
    print(i, i*sgn, s)
    sgn = -sgn
print(s)

n =randint(5, 15) * 2 + 1
genres = "♂♀"
seq = ""
for i in range(n):
    seq += genres[randint(0, 1)]
print(f"Nouveaux lapereaux ? {seq}")
males = 0
femelles = 0
for i in range(len(seq)):
    if seq[i] == "♂":
        males += 1
    else:
        femelles += 1
print(f"{n} lapereaux")
print(f"{males} males")
print(f"{femelles} femelles")
