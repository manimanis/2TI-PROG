from random import randint

msg1 = input("Message à crypter ? ")
seq = ""
for i in range(26):
    seq += chr(65 + i)
print(seq)
for i in range(26):
    a = i
    b = randint(0, len(seq) - 1)
    if b < a:
        t = a
        a = b
        b = t
    if a != b:
        seq = seq[:a] + seq[b] + seq[a+1:b] + seq[a] + seq[b+1:]
msg2 = ""
for i in range(len(msg1)):
    if "A" <= msg1[i] <= "Z":
        msg2 += seq[ord(msg1[i]) - 65]
    else:
        msg2 += msg1[i]
print("Clé :", seq)
print("Message clair  : ", msg1)
print("Message crypté : ", msg2)