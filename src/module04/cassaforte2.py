count = 0
for m in range(1, 10):
    for c in range(1, 9):
        for d in range(1, 9):
            for u in range(1, 9):
                if c > d >= m >= u and (m*u) % 7 == (c*d) % 7:
                    print(m,c,d,u)
                    count += 1
print(count)