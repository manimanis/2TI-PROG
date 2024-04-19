
def saisie(min):
   n = int(input(f"Nombre >={min} ? "))
   while n < min:
      n = int(input(f"Nombre >={min} ? "))
   return n

def est_armstrong(n):
   n1 = n
   o = len(str(n))
   s = 0
   while n1 > 0:
      digit = n1 % 10
      s += digit ** o
      n1 //= 10
   return n == s

a = saisie(10)
b = saisie(a)
for i in range(a, b + 1):
   if est_armstrong(i):
      print(i,"is an Armstrong number")