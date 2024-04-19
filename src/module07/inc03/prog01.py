# seq 1
n = int(input("Nombre >= 100 ? "))
while n < 100:
    n = int(input("Nombre >= 100 ?"))
# seq 2
n1 = n
o = len(str(n))
s = 0
while n1 > 0:
   digit = n1 % 10
   s += digit ** o
   n1 //= 10
# seq 3
if n == s:
   print(n,"est un nombre Armstrong.")
else:
   print(n,"est un nombre Armstrong.")