# Evaluation groupe 1
#---------------------------------

# Page 1 - Question 1
ch1 = "L'eau est la vie"
ch2 = "essentielle pour"
p = ch1.find("la")
ch3 = ch1[:p] + ch2 + ch1[p-1:]
print("Question 1")
print(p)
print(ch3)
print()


# Page 1 - Question 2
a = 763124
b = a // 10 % 1000
print("Question 2")
print(b)
print()


# Page 1 - Question 3
x = 4
y = 6
z = (x+y) // 3 * x + y % x + (y != x) / 2
w = z - int(z)
print("Question 3")
print(z, type(z))
print(w)
print()


# Page 1 - Question 4
n1 = "17"
n2 = "181"
n3 = "252629"
n4 = int(n1[1] + "0" + n2[1] + "0" + n3[5] + "0")
print("Question 4")
print(n4)
print()


# Page 1 - Question 5
ch = "Stylesheet"
car = chr(ord(ch[len(ch) // 2]) + 1)
p = ch.find(car)
print("Question 5")
print(car)
print(p)
print()

# Evaluation groupe 2
#---------------------------------


# Page 2 - Question 1
ch1 = "Il n'y a pas de honte, ni de soucis, à préférer le bonheur !"
ch2 = "ni de soucis"
p = ch1.find(ch2)
ch3 = ch1[:p-2] + ch1[p+len(ch2)+1:]
print("Question 1")
print(p, p-2, p+len(ch2)+1)
print(ch3)
print()


# Page 2 - Question 2
a = 763124
c = a // 10 % 10
d = a // 10000 % 10
e = a // 100000
b = c * 100 + d * 10 + e
print("Question 2")
print(b)
print()


# Page 2 - Question 3
x = 5
y = 8
z = (x+y) % 3 * x + y * y // x + (y <= x) * 2.0
w = z - int(z)
print("Question 3")
print(z, type(z))
print(w)
print()


# Page 2 - Question 4
n1 = "17"
n2 = "181"
n3 = "252629"
n4 = int(n1[1] + n2[1] + n3[5] + "00")
print("Question 4")
print(n4)
print()


# Page 2 - Question 5
ch = "Stylesheet"
car = chr(ord(ch[len(ch) - 1]) - 1)
p = ch.find(car)
print("Question 5")
print(car)
print(p)
print()