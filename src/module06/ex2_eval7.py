def ConvCh(n):
    return str(n)

def sous_chaine(ch, d, f):
    return ch[d:f]

def Long(ch):
    return len(ch)

def Pos(sch, ch):
    return ch.find(sch)

def valeur(ch):
    return int(ch)

def effacer(ch, d, f):
    return ch[:d] + ch[f:]

T1 = [str()]*5
T2 = [int()]*5

ch1 = "James Webb Space Telescope"
ch2 = "NASA/ESA/CSA"

T1[4] = sous_chaine(ch1, Long(ch2)-1, Long(ch1))
T1[0] = ch1[0] + ch1[6] + T1[4][0] + T1[4][6]
T1[3] = effacer(ch2, Pos("E", ch2) - 1, Long(ch2))
T1[1] = ch2[3] + sous_chaine(ch2, 0, 3)
T1[2] = ConvCh(Long(ch2)) + ConvCh(Long(ch1))

print(T1)

T2[0] = Long(ch1) + Long(ch2)
T2[4] = Pos("S", ch2)
T2[1] = T2[0] + T2[4] + abs(T2[4] - T2[0]) // 2
T2[2] = (T2[1] % T2[0]) * 100 + T2[4] * 10 + T2[0] // 10 + 1
T2[3] = ord(ch1[0]) - 65 + valeur(T1[2]) % 100

print(T2)