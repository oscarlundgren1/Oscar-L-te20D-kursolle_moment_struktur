#Denna applikation gör ett antal beräkningar på en rektangel/rätblock.

print("Denna applikation gör ett antal beräkningar på en rektangel/rätblock.\nAnge dina 3 sidor, endast heltal är tillåtet\n")
while True:
    side1=int(input("Ange rektangelns ena sida: "))
    side2=int(input("Ange rektangelns andra sida: "))
    height=int(input("Ange rätblockets höjd: "))#Ber om ett värde på höjden
    area=side1*side2
    a = "-"
    y = "|"
    print(f"Rektangeln har sidorna {side1} och {side2} vilket gör att arean är {area}")

    if side1 == side2:
        print("Eftersom bägge sidorna är lika långa så är denna rektangel en kvadrat.")
    else:
        print("Eftersom sidorna är olika stora är denna en rektangel.")

    if height < 1:
        print("Höjden | Volymen")
        print(f"{a:-^17}")
        for i in range (1, 1+1):#Höjden bestämmer hur mycket i tabellen som visas
            b = i*25
            print("{0: >7} |{1: >7}".format(i,b))
    elif height > 11:
        print("Höjden | Volymen")
        print(f"{a:-^17}")
        for i in range (1, 10+1):#Höjden bestämmer hur mycket i tabellen som visas
            b = i*25
            print("{0: >7} |{1: >7}".format(i,b))
    else:
        print("Höjden | Volymen")
        print(f"{a:-^17}")
        for i in range (1, height+1):#Höjden bestämmer hur mycket i tabellen som visas
            b = i*25
            print("{0: >7} |{1: >7}".format(i,b))
    repeat=input("Vill du göra en beräkning till (J/N)?")
    if repeat == "J":
        print("Programmet körs igen\n")
    else:
        print("Programmet avsultas...\n")
        exit()