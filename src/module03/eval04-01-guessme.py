from random import randint, seed

seed(5)
# for i in range(5):
#     print(randint(10, 99))

n1 = int(input("Choisir un nbre [10, 99] ? "))
u1 = n1 % 10  # Chiffre des unités
d1 = n1 // 10 # Chiffre des dizaines
n2 = randint(10, 99) # nombre aléatoire [10, 99]
u2 = n2 % 10  # Chiffre des unités
d2 = n2 // 10 # Chiffre des dizaines
if n1 == n2:
    score = 200
elif u1 == d2 and d1 == u2:
    score = 100
elif u1 == d2 or u1 == u2 or d1 == u2 or d1 == d2:
    score = 50
else:
    score = 0
print("L’ordinateur a choisi :", n2)
print("Score :", score)