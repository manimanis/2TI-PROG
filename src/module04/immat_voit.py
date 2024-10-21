im1 = input("Immatriculation voiture 1 ? ")
im2 = input("Immatriculation voiture 2 ? ")

im1 = im1.upper()
im2 = im2.upper()

p1 = im1.find("TU")
p2 = im2.find("TU")

if p1 == -1 or p2 == -1:
    print("Immatriculation incorrecte!")
    exit()

o1 = int(im1[:p1])
s1 = int(im1[p1 + 2 :])
o2 = int(im2[:p2])
s2 = int(im2[p2 + 2 :])

if s2 < s1:
    print(im2, "est plus vieille que", im1)
elif s2 > s1:
    print(im1, "est plus vieille que", im2)
elif o2 < o1:
    print(im2, "est plus vieille que", im1)
elif o2 > o1:
    print(im1, "est plus vieille que", im2)
else:
    print("Même matricule, même voiture.")