pos = input("Position fou ? ")
dir = input("Direction (U: Up, D: Down, R: Right, L: Left) ? ")
pas = int(input("Nombre pas ? "))

if len(pos) != 2 or pos[0] < "a" or pos[0] > "h" or pos[1] < "1" or pos[1] > "8":
    print("Position incorrecte")
elif len(dir) != 2 or dir[0] not in ["U", "D"] or dir[1] not in ["R", "L"]:
    print("Direction incorrecte")
else:
    px = ord(pos[0]) - 96
    py = int(pos[1])
    dy = (dir[0] == "U") - (dir[0] == "D")
    dx = (dir[1] == "R") - (dir[1] == "L")
    px += pas * dx
    py += pas * dy
    if 1 <= px <= 8 and 1 <= py <= 8:
        pos1 = chr(96 + px) + str(py)
        print("Nouvelle position :", pos1)
    else:
        print("La pièce sort de l'échiquier")
