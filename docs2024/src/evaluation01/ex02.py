qf = float(input("Quantité fraise (litre) ? "))
qp = float(input("Quantité pêche (litre) ? "))
qb = float(input("Quantité banane (litre) ? "))
qt = qf + qp + qb
prix = 10 * qf + 15 * qp + 25 * qb
pl = prix / qt
print("Quantité totale jus (litre) : ", qt, 'litres')
print("Prix total à payer", prix, "DT")
print("Prix d'un litre de jus", pl, "DT")