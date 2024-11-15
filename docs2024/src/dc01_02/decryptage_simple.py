from random import randint

msg1 = input("Message crypté ? ")
cle = input("Clé ? ")
msg2 = ""
for i in range(len(msg1)):
    if "A" <= msg1[i] <= "Z":
        p = cle.find(msg1[i]) + 65
        msg2 += chr(p)
    else:
        msg2 += msg1[i]
print("Clé :", cle)
print("Message crypté : ", msg1)
print("Message clair  : ", msg2)
