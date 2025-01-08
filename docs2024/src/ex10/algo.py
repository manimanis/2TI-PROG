def majus(ch: str):
    return ch.upper()

def sous_chaine(ch: str, d: int, f: int):
    return ch[d:f]

def effacer(ch: str, d: int, f: int):
    return ch[:d] + ch[f:]

def convch(v):
    return str(v)

def valeur(x):
    try:
        return int(x)
    except:
        return float(x)

def pos(ch1, ch2):
    return ch2.find(ch1)

def long(ch: str):
    return len(ch)

def ent(x: float):
    return int(x)

def alea(vi: int, vf: int):
    from random import randint
    return randint(vi, vf)
