import sys

write_txt = open("Battleship.out", "w")
txt1 = open(sys.argv[1], "r", encoding="utf-8")
txt2 = open(sys.argv[2], "r", encoding="utf-8")
in1 = open(sys.argv[3], "r", encoding="utf-8")
in2 = open(sys.argv[4], "r", encoding="utf-8")
r_in1 = in1.read().split(";")
r_in2 = in2.read().split(";")
r_txt1 = txt1.readlines()
r_txt2 = txt2.readlines()
grid1 = []
for i in range(len(r_txt1)):
    if i == 9:
        grid1.append([str(i + 1) + "-", *"-" * (len(r_txt1) - 1)])
    else:
        grid1.append([str(i + 1), *"-" * len(r_txt1)])

for j in range((len(grid1)) - 1):
    line = r_txt1[j]
    diff1 = 0
    index_item1 = 1
    for item in line:
        if item == "\n":
            pass
        elif item != ";":
            grid1[j][index_item1 - diff1] = item
            diff1 += 1
        index_item1 += 1
diff1_ = 1
index_item1_ = 1
for i in range(len(r_txt1[9])):
    item = r_txt1[9][i]
    if item != ";":
        if i == 0:
            grid1[9][0] = f"10{item}"
            diff1_ += 1
        else:
            grid1[9][index_item1_ - diff1_] = item
            diff1_ += 1
    index_item1_ += 1
grid2 = []
for i in range(len(r_txt2)):
    if i == 9:
        grid2.append([str(i + 1) + "-", *"-" * (len(r_txt2) - 1)])
    else:
        grid2.append([str(i + 1), *"-" * len(r_txt2)])
for j in range((len(grid2)) - 1):
    line = r_txt2[j]
    diff2 = 0
    index_item2 = 1
    for item in line:
        if item == "\n":
            pass
        elif item != ";":
            grid2[j][index_item2 - diff2] = item
            diff2 += 1
        index_item2 += 1
diff2_ = 1
index_item2_ = 1
for i in range(len(r_txt2[9])):
    item = r_txt2[9][i]
    if item != ";":
        if i == 0:
            grid2[9][0] = f"10{item}"
            diff2_ += 1
        else:
            grid2[9][index_item2_ - diff2_] = item
            diff2_ += 1
    index_item2_ += 1
    ship_type_1 = set([])
for i in range(9):
    if i == 9:
        for j in range(10):
            if j == 0:
                if grid1[i][j] != "10-":
                    ship_type_1.add(str(grid1[i][j][-1]))
            else:
                if grid1[i][j] != "-":
                    ship_type_1.add(str(grid1[i][j]))
    else:
        for j in range(1, 11):
            if grid1[i][j] != "-":
                ship_type_1.add(str(grid1[i][j]))

ship_type_2 = set([])
for i in range(9):
    if i == 9:
        for j in range(10):
            if j == 0:
                if grid2[i][j] != "10-":
                    ship_type_2.add(str(grid2[i][j][-1]))
            else:
                if grid2[i][j] != "-":
                    ship_type_2.add(str(grid2[i][j]))
    else:
        for j in range(1, 11):
            if grid2[i][j] != "-":
                ship_type_2.add(grid2[i][j])

ship_location1 = {}
for shiptype in ship_type_1:
    ship_location1[shiptype] = []
ship_location2={}
for shiptype in ship_type_2:
    ship_location2[shiptype] = []

for i in range(10):
    a = 1
    if i == 9:
        itemindex = 1
        for item in grid1[i]:
            if len(item) > 1 and item != "10-":
                ship_location1[str(item[-1])].append((i, 1))
            elif len(item) == 1 and item != "-":
                ship_location1[str(item)].append((i + 1, itemindex))
            itemindex += 1
    else:
        for item in grid1[i][1:]:
            if item != "-":
                ship_location1[item].append((i + 1, a))
                a += 1
            else:
                a += 1
for i in range(10):
    a = 1
    if i == 9:
        itemindex = 1
        for item in grid2[i]:
            if len(item) > 1 and item != "10-":
                ship_location2[str(item[-1])].append((i, 1))
            elif len(item) == 1 and item != "-":
                ship_location2[str(item)].append((i + 1, itemindex))
            itemindex += 1
    else:
        for item in grid2[i][1:]:
            if item != "-":
                ship_location2[item].append((i + 1, a))
                a += 1
            else:
                a += 1
for ship in ship_location1:
    if ship == "B":
        B_ship1 = [[] for i in range(int(len(ship_location1[ship]) / 4))]
        a = 0
        b = 4

        for sublist_B in B_ship1:
            sublist_B.append(ship_location1[ship][a:b])
            a += 4
            b += 4

    if ship == "P":
        P_ship1 = set([])
        a = 0
        b = 2

        for i in range(len(ship_location1[ship])):
            c, d = ship_location1[ship][i]
            if (c, d + 1) in ship_location1[ship]:
                P_ship1.add(((c, d), (c, d + 1)))
            if (c, d - 1) in ship_location1[ship]:
                P_ship1.add(((c, d), (c, d - 1)))
            if (c + 1, d) in ship_location1[ship]:
                P_ship1.add(((c, d), (c + 1, d)))
            if (c - 1, d) in ship_location1[ship]:
                P_ship1.add(((c, d), (c - 1, d)))
        main_dict1 = {}

        for tuples in P_ship1:
            if tuples[0] not in main_dict1.keys() and tuples[0] not in main_dict1.values():
                main_dict1[tuples[0]] = tuples[1]
for ship in ship_location2:
    if ship == "B":
        B_ship2 = [[] for i in range(int(len(ship_location2[ship]) / 4))]
        a = 0
        b = 4

        for sublist_B in B_ship2:
            sublist_B.append(ship_location2[ship][a:b])
            a += 4
            b += 4

    if ship == "P":
        P_ship2 = set([])
        a = 0
        b = 2

        for i in range(len(ship_location1[ship])):
            c, d = ship_location2[ship][i]
            if (c, d + 1) in ship_location2[ship]:
                P_ship2.add(((c, d), (c, d + 1)))
            if (c, d - 1) in ship_location2[ship]:
                P_ship2.add(((c, d), (c, d - 1)))
            if (c + 1, d) in ship_location2[ship]:
                P_ship2.add(((c, d), (c + 1, d)))
            if (c - 1, d) in ship_location2[ship]:
                P_ship2.add(((c, d), (c - 1, d)))
        main_dict2 = {}

        for tuples in P_ship2:
            if tuples[0] not in main_dict2.keys() and tuples[0] not in main_dict2.values():
                main_dict2[tuples[0]] = tuples[1]
alp = " ABCDEFGHIJ"
#---------------------------------------------------------------------------------
hidden1 = []
for i in range(len(r_txt1)):
    if i == 9:
        hidden1.append([str(i + 1) + "-", *"-" * (len(r_txt1) - 1)])
    else:
        hidden1.append([str(i + 1), *"-" * len(r_txt1)])

for j in range(len(r_in1)):
    try:
        x = int(r_in1[j][0]) - 1
        y = alp.index(r_in1[j][2]) + 1
        if x == 9:
            if y == 1:
                if grid1[9][0] != "10-":
                    hidden1[9][0] = f"10{'X'}"
                else:
                    hidden1[9][0] = f"1O{'O'}"
            elif y != 1:
                if grid1[9][y - 1] != "-":
                    hidden1[9][y - 1] = "X"
                else:
                    hidden1[x][y] = "O"
        elif x != 9 and grid1[x][y - 1] != "-":
            hidden1[x][y] = "X"
        elif x != 9 and grid1[x][y - 1] == "-":
            hidden1[x][y] = "O"

    except Exception:
        pass
hidden2 = []
for i in range(len(r_txt2)):
    if i == 9:
        hidden2.append([str(i + 1) + "-", *"-" * (len(r_txt2) - 1)])
    else:
        hidden2.append([str(i + 1), *"-" * len(r_txt2)])

for j in range(len(r_in2)):
    try:
        x = int(r_in2[j][0]) - 1
        y = alp.index(r_in2[j][2]) + 1
        if x == 9:
            if y == 1:
                if grid2[x][y - 1][2] != "-":
                    hidden2[x][y - 1][2] = "X"
                else:
                    hidden2[x][y - 1][2] = "O"
            else:
                if grid2[x][y - 1] != "-":
                    hidden2[x][y - 1] = "X"
                else:
                    hidden2[x][y - 1] = "O"

        elif grid2[x][y] != "-":
            hidden2[x][y] = "X"
        elif grid2[x][y] == "-":
            hidden2[x][y] = "O"
    except Exception:
        pass
#-------------------------------------------------------------------------------
bomb_ = {}
bugbomb_ = {}
bomb_["player1's attack"] = []
bomb_["player2's attack"] = []
for i in range(len(r_in1)):
    try:
        x1 = int(r_in1[i].split(",")[0])
        y1 = alp.index(r_in1[i].split(",")[1])
        bomb_["player1's attack"].append((x1, y1))
    except Exception:
        i += 1
for i in range(len(r_in2)):
    try:
        x2 = int(r_in2[i].split(",")[0])
        y2 = alp.index(r_in2[i].split(",")[1])
        bomb_["player2's attack"].append((x2, y2))
    except Exception:
        i += 1

hidden1_ = []
for i in range(10):
    if i == 9:
        hidden1_.append([str(i + 1) + "-", *"-" * 9])
    else:
        hidden1_.append([str(i + 1), *"-" * 10])
hidden2_ = []
for i in range(10):
    if i == 9:
        hidden2_.append([str(i + 1) + "-", *"-" * 9])
    else:
        hidden2_.append([str(i + 1), *"-" * 10])
#--------------------------------------------------------------------------------
pass_ = 0
c1, d1, p1, s1, b1 = ["-"], ["-"], ["-", "-", "-", "-"], ["-"], ["-", "-"]
c2, d2, p2, s2, b2 = ["-"], ["-"], ["-", "-", "-", "-"], ["-"], ["-", "-"]
cc, ccc, dd, ddd, ss, sss = 0, 0, 0, 0, 0, 0
for i in range(len(bomb_["player1's attack"])):
    try:
        _x2 = bomb_["player2's attack"][i][0] - 1
        _y2 = bomb_["player2's attack"][i][1]
        _x1 = bomb_["player1's attack"][i][0] - 1
        _y1 = bomb_["player1's attack"][i][1]
        if _x1 == 9:
            if hidden2_[_x1][_y1 - 1] != "-":
                pass_ += 1
            elif _y1 == 1:
                if grid2[_x1][_y1 - 1] != "10-":
                    hidden2_[_x1][_y1 - 1] = f"10{'X'}"
                elif grid2[_x1][_y1 - 1] == "10-":
                    hidden2_[_x1][_y1 - 1] = f"10{'O'}"
            else:
                if grid2[_x1][_y1 - 1] != "-":
                    hidden2_[_x1][_y1 - 1] = "X"
                elif grid2[_x1][_y1 - 1] == "-":
                    hidden2_[_x1][_y1 - 1] = "O"
        else:
            if hidden2_[_x1][_y1] != "-":
                pass_ += 1
            else:
                if grid2[_x1][_y1] != "-":
                    hidden2_[_x1][_y1] = "X"
                elif grid2[_x1][_y1] == "-":
                    hidden2_[_x1][_y1] = "O"

        for k in ship_location2["C"]:
            if hidden2_[k[0]][k[1]] == "X":
                ccc += 1
        if ccc == 5:
            c1.pop(0)
            c1.append("X")


        print("""
Player1's Move
        
Round : {}\t\t\t\t\tGrid Size:10x10

Player1's Hidden Board		Player2's Hidden Board
  A B C D E F G H I J		  A B C D E F G H I J""".format(i + 1))
        write_txt.write("""
Player1's Move

Round : {}\t\t\t\t\tGrid Size:10x10

Player1's Hidden Board		Player2's Hidden Board
  A B C D E F G H I J		  A B C D E F G H I J\n""".format(i + 1))
        for j in range(10):
            print(" ".join(hidden1_[j]), "\t\t", " ".join(hidden2_[j]))
            write_txt.write(" ".join(hidden1_[j]) + "\t\t" + " ".join(hidden2_[j]) + "\n")
        print(""" 
Carrier		""" + ' '.join(c1) + """\t\t\t\tCarrier		""" + ' '.join(c2) + """
Battleship	""" + ' '.join(b1) + """\t\t\t\tBattleship	""" + ' '.join(b2) + """
Destroyer	""" + ' '.join(d1) + """\t\t\t\tDestroyer	""" + ' '.join(d2) + """
Submarine	""" + ' '.join(s1) + """\t\t\t\tSubmarine	""" + ' '.join(s2) + """
Patrol Boat	""" + ' '.join(p1) + """\t\t\tPatrol Boat	""" + ' '.join(p2) + "\n")
        #print("Enter your move :",r_txt[i])
        write_txt.write(""" 
Carrier		""" + ' '.join(c1) + """\t\t\t\tCarrier		""" + ' '.join(c2) + """
Battleship	""" + ' '.join(b1) + """\t\t\t\tBattleship	""" + ' '.join(b2) + """
Destroyer	""" + ' '.join(d1) + """\t\t\t\tDestroyer	""" + ' '.join(d2) + """
Submarine	""" + ' '.join(s1) + """\t\t\t\tSubmarine	""" + ' '.join(s2) + """
Patrol Boat	""" + ' '.join(p1) + """\t\t\tPatrol Boat	""" + ' '.join(p2) + "\n")

        if _x2 == 9:
            if hidden1_[_x2][_y2 - 1] != "-":
                pass_ += 1
            elif _y2 == 1:
                if grid1[_x2][_y2 - 1] != "10-":
                    hidden1_[_x2][_y2 - 1] = f"10{'X'}"
                elif grid1[_x2][_y2 - 1] == "10-":
                    hidden1_[_x2][_y2 - 1] = f"10{'O'}"

            else:
                if grid1[_x2][_y2 - 1] != "-":
                    hidden1_[_x2][_y2 - 1] = "X"
                elif grid1[_x2][_y2 - 1] == "-":
                    hidden1_[_x2][_y2 - 1] = "O"
        else:
            if hidden1_[_x2][_y2] != "-":
                pass_ += 1

            else:
                if grid1[_x2][_y2] != "-":
                    hidden1_[_x2][_y2] = "X"
                elif grid1[_x2][_y2] == "-":
                    hidden1_[_x2][_y2] = "O"

        for k in ship_location1["C"]:
            if k[0]==10 and k[1]==1:
                if hidden1_[k[0]][k[1]-1]=="X":
                    cc+=1

            elif hidden1_[k[0]][k[1]] == "X":
                cc += 1
        if cc == 5:
            c2.pop(0)
            c2.append("X")

        print("""
Player2's Move
        
Round : {}\t\t\t\t\tGrid Size:10x10

Player1's Hidden Board		Player2's Hidden Board
  A B C D E F G H I J		  A B C D E F G H I J""".format(i + 1))
        write_txt.write("""
Player2's Move

Round : {}\t\t\t\t\tGrid Size:10x10

Player1's Hidden Board		Player2's Hidden Board
  A B C D E F G H I J		  A B C D E F G H I J\n""".format(i + 1))
        for j in range(10):
            print(" ".join(hidden1_[j]), "\t\t", " ".join(hidden2_[j]))
            write_txt.write(" ".join(hidden1_[j]) + "\t\t" + " ".join(hidden2_[j]) + "\n")
        print(""" 
Carrier		""" + ' '.join(c1) + """\t\t\t\tCarrier		""" + ' '.join(c2) + """
Battleship	""" + ' '.join(b1) + """\t\t\t\tBattleship	""" + ' '.join(b2) + """
Destroyer	""" + ' '.join(d1) + """\t\t\t\tDestroyer	""" + ' '.join(d2) + """
Submarine	""" + ' '.join(s1) + """\t\t\t\tSubmarine	""" + ' '.join(s2) + """
Patrol Boat	""" + ' '.join(p1) + """\t\t\tPatrol Boat	""" + ' '.join(p2) + "\n")
        #print("Enter your move :",r_txt2[i])
        write_txt.write(""" 
Carrier		""" + ' '.join(c1) + """\t\t\t\tCarrier		""" + ' '.join(c2) + """
Battleship	""" + ' '.join(b1) + """\t\t\t\tBattleship	""" + ' '.join(b2) + """
Destroyer	""" + ' '.join(d1) + """\t\t\t\tDestroyer	""" + ' '.join(d2) + """
Submarine	""" + ' '.join(s1) + """\t\t\t\tSubmarine	""" + ' '.join(s2) + """
Patrol Boat	""" + ' '.join(p1) + """\t\t\tPatrol Boat	""" + ' '.join(p2) + "\n")
    except Exception:
        pass
#---------------------------------------------------------------------------------------
for i in range(10):
    if i == 9:
        for j in range(10):
            if j == 0:
                if grid1[i][j] != "10-" and hidden1_[i][j] == "10-":
                    hidden1_[i][j] = grid1[i][j]
            else:
                if grid1[i][j] != "-" and hidden1_[i][j] == "-":
                    hidden1_[i][j] = grid1[i][j]

    else:
        for j in range(1, 11):
            if grid1[i][j] != "-" and hidden1_[i][j] == "-":
                hidden1_[i][j] = grid1[i][j]
for i in range(9):
    if i == 9:
        for j in range(10):
            if j == 0:
                if grid2[i][j] != "10-" and hidden2_[i][j] == "10-":
                    hidden2_[i][j] = grid2[i][j]
            else:
                if grid2[i][j] != "-" and hidden2_[i][j] == "-":
                    hidden2_[i][j] = grid2[i][j]
    else:
        for j in range(1, 11):
            if grid2[i][j] != "-" and hidden2_[i][j] == "-":
                hidden2_[i][j] = grid2[i][j]
#------------------------------------------------------------------------------------------
print("Final information:\n")
write_txt.write("\nFinal information:\n\n")
print("  A B C D E F G H I J		  A B C D E F G H I J")
write_txt.write("  A B C D E F G H I J		  A B C D E F G H I J\n")
for i in range(10):
    print(" ".join(hidden1_[i]), "\t\t", " ".join(hidden2_[i]))
    write_txt.write(" ".join(hidden1_[i]) + "\t\t" + " ".join(hidden2_[i]) + "\n")
print(""" 
Carrier		""" + ' '.join(c1) + """\t\t\t\tCarrier		""" + ' '.join(c2) + """
Battleship	""" + ' '.join(b1) + """\t\t\t\tBattleship	""" + ' '.join(b2) + """
Destroyer	""" + ' '.join(d1) + """\t\t\t\tDestroyer	""" + ' '.join(d2) + """
Submarine	""" + ' '.join(s1) + """\t\t\t\tSubmarine	""" + ' '.join(s2) + """
Patrol Boat	""" + ' '.join(p1) + """\t\t\tPatrol Boat	""" + ' '.join(p2) + "\n")
write_txt.write(""" 
Carrier		""" + ' '.join(c1) + """\t\t\t\tCarrier		""" + ' '.join(c2) + """
Battleship	""" + ' '.join(b1) + """\t\t\t\tBattleship	""" + ' '.join(b2) + """
Destroyer	""" + ' '.join(d1) + """\t\t\t\tDestroyer	""" + ' '.join(d2) + """
Submarine	""" + ' '.join(s1) + """\t\t\t\tSubmarine	""" + ' '.join(s2) + """
Patrol Boat	""" + ' '.join(p1) + """\t\t\tPatrol Boat	""" + ' '.join(p2) + "\n")


