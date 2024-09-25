x = float(input("Coût au m² ? "))
a = float(input("a en m ? "))
b = float(input("b en m ? "))
c = float(input("c en m ? "))
d = float(input("d en m ? "))
qte = 2*d*(a+b) + a*c + b*(a*a+4*c*c)**0.5
aire = a * b
cout = x * qte
print("L'aire sous la tente est", round(aire, 1), "m²")
print("La tente nécessite", round(qte, 1), "m² de matériaux.")
print("la tente coûte", round(cout, 3), "DT")
