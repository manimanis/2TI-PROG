def convch(v):
    return str(v)

Convch = convch

def souschaine(ch, d, f):
    return ch[d:f]


def valeur(ch, fn=int):
    return fn(ch)


def pos(ch1, ch):
    return ch.find(ch1)

def effacer(ch, d, f):
    return ch[:d] + ch[f:]

def Long(ch):
    return len(ch)

long=Long