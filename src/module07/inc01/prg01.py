# seq 1
mot = input("Donner un mot ? ")
while len(mot) <= 3:
    mot = input("Donner un mot ? ")

# seq 2
cars = ""
for i in range(65, 91):
    if mot.find(chr(i)) != -1 and cars.find(chr(i)) == -1:
        cars += chr(i)

# seq 3
print(cars)