import os

cur_dir = os.path.dirname(__file__)
file = os.path.join(cur_dir, "texte.txt")

dct = {}
for i in range(65, 91):
    dct[chr(i)] = 0

lettres = 0
with open(file, "r") as f:
    for line in f:
        line = line.strip().upper()
        for car in line:
            if "A" <= car <= "Z":
                lettres += 1
                dct[car] += 1

for i in range(65, 91):
    print(round(dct[chr(i)] * 100 / lettres, 1),end="\t")

