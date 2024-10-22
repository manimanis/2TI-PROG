for a in range(1, 9):
    for b in range(0, 9):
        for c in range(0, 9):
            for d in range(0, 9):
                s = a + b + c + d
                n = a * 1000 + b * 100 + c * 10 + d
                if n % s == 0:
                    print(n, s)
