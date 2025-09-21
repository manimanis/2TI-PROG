def saisie():
    mot = input("Donner un mot ? ")
    while len(mot) <= 3:
        mot = input("Donner un mot ? ")
    return mot

# seq 2
def lettres(mot):
    cars = ""
    for i in range(65, 91):
        if mot.find(chr(i)) != -1 and cars.find(chr(i)) == -1:
            cars += chr(i)
    return cars

# seq 3
mot1 = saisie()
mot2 = saisie()

cars1 = lettres(mot1)
cars2 = lettres(mot2)

print(mot1, cars1)
print(mot2, cars2)

if cars1 == cars2:
    print("Les mots contiennent les mêmes lettres")
else:
    print("Les mots ne contiennent pas les mêmes lettres")