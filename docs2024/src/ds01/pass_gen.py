P = input("Prénom ? ")
N = input("Identifiant ? ")
s1 = 0
for i in range(0, len(P), 2):
    s1 += ord(P[i])
s2 = 0
for i in range(len(N)):
    v = int(N[i])
    if v % 2 == 1:
        s2 += v
C = s1 - s2
print(f"s1 = {s1} - s2 = {s2} - C = {C}")
pwd = P[-5:] + str(C)
print("Mot de passe :", pwd)

"""
HALLOUMA
94321785
"""