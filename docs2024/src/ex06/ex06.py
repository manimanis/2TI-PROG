from algo import *

ch1 = "Google Walland"
ch2 = "My friend"
ch3 = "You are a nice guy"
ch4 = "nice"
v1 = 10
v2 = -19

a = ch1[7] == chr(87) and ord(majus(ch1[2])) > ord(ch1[5]) and ord(ch1[5]) == ord(chr(101))
b = effacer(ch2, pos("f", ch2), long(ch2)) + sous_chaine(ch1, pos("all", ch1) - 1, long(ch1))
c = chr(valeur(convch(pos(" ", ch1)) + convch(pos("i", ch2))))
d = ch1[7] + ch2[6] + ch1[6] + sous_chaine(ch1, 0, 2)
e = long(ch2 + "'s " + ch1)
f = pos(ch4, ch3)
g = sous_chaine(ch3, 0, f) + "lucky" + sous_chaine(ch2, long(ch4) // 2, long(ch2)) + "."
h = valeur(convch(v1 // 2) + convch(v1 / 20) + convch(v1 % 4) + convch(ent(10*3.75)))
i = (v2 % 5) * 100 + (v2 // 5 % 5) * 10 + v2 // 25
j = 15 <= alea(1, 6) * 5 <= 25

vars = "abcdefghij"
for var in vars:
    tp = str(type(globals()[var])).split("'")[1]
    val = ('"' if tp == "str" else '') + str(globals()[var]) + ('"' if tp == "str" else '')
    print(var, "=", val, f"({tp})")