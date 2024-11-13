n  = int(input("donner n ? "))
ne = 2*n-1
ch = ""
for i in range(n-1):
    ch = ch + " "
ch = ch + "*"
print(ch)
for i in range(n-1):
    ch = ch[1:len(ch)]+"**"
    print(ch)

nl = 2*n-1
ch = ""
for i in range(nl):
    if i<n:
        ch = ch + "*"
    else:
        ch = ch[1:]
    print(ch)

nl = 2*n-1
ch = ""
for i in range(n-1):
    ch = ch + " "
ch = ch + "*"
print(ch)
for i in range(nl-1):
    if i<n-1:
        ch = ch[1:]+"*"
    else:
        ch = " "+ch[:-1]
    print(ch)

ch = ""
for i in range(n):
    ch = ch + "*"
    print(ch)
for i in range(n-1):
    print(ch[:n-i-1])