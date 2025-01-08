from algo import *
ch1 = "Orion"
ch2 = "Andromeda"
T1 = [""]*5
T1[0] = ch1[0]                
T1[1] = ch1[long(ch1) // 2]
T1[2] = sous_chaine(ch1, 0, 4)
T1[3] = effacer(sous_chaine(ch2, 2, 7), 1, 2)
T1[4] = majus(ch2[3]) + sous_chaine(T1[3], 1, 4)
print(T1)

T2 = [0]*5
T2[0] = long(T1[2]) + long(T1[4])
T2[1] = (T2[0] % 2 == 0) * (T2[0] // 2) + (T2[0] % 2 != 0) * T2[0]
T2[2] = valeur(convch(T2[1]) + '5')
T2[3] = ord(T1[0]) + ord(T1[1])
T2[4] = abs(T2[3] - len(T1[4]))
print(T2)