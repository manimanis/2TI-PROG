n = int(input("Donner un nombre ? "))
if n < 1000 or n > 9999:
    print("Nombre incorrect")
else:
    m = n // 1000
    c = n // 100 % 10
    d = n // 10 % 10
    u = n % 10
    s = m + c + d + u
    if n % 2 == 0:
        print(n, "est pair.")
    else:
        print(n, "est impair.")
    
    if n % s == 0:
        print(n, "est harshad.")
    else:
        print(n, "n'est pas harshad.")
