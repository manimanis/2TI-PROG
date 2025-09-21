def EstGagnant(numtel, fete):
    gagne = True
    for i in range(len(fete)):
        if numtel.find(fete[i]) == -1:
            gagne = False
    return gagne

a = "52743694"
b = "94543693"
c = "203" 
d = 93504687
e = 74
print(EstGagnant(a, "257"))
print(EstGagnant("94543693", c))
#print(EstGagnant(int(b), int(c)))
print(EstGagnant(str(d), str(e)))
print(EstGagnant(str(1/7), chr(49)+chr(53)))
print(EstGagnant(b[4:]+a[4:],"74"))

