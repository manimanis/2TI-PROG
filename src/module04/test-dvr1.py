from algo import *

s1 = "soleil"
s2 = "terre"
v1 = 3
v2 = 1530
tm = v2 // (v1 * 60)           # ………………………
ts = (v2 % (v1 * 60)) // v1  # ………………………
time = Convch(tm) + chr(58) + Convch(ts) # ………………………
mot1 = effacer(s2, 0, 3)+s1[0]+s2[0]+s1[1]+souschaine(s2, 3, 5) # "restore"
mot2 = s2[2]+souschaine(s1, 1, Long(s1) // 2+1)         # ………………………
mot3 = chr(ord(mot2[0]) - 2) + effacer(mot2, 0, 1) # "pole"
v3 = valeur(effacer(time, 1, 2))       # ………………………
v4 = ((v3 - ts) // 100) * 60          # ………………………
v5 = v4 != (tm * 60)                    # ………………………
v6 = pos(souschaine(s1,2,4), mot3) == (pos(mot1[1], s1)-1) # ………………………
print()