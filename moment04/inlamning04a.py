#Denna applikation gör ett antal beräkningar på en rektangel/rätblock

print("Denna applikation gör ett antal beräkningar på en rektangel/rätblock.\nAnge dina 2 sidor, endast heltal är tillåtet\n")
side1=int(input("Ange rektangelns ena sida: "))#Ber om ett värde på en sida
side2=int(input("Ange rektangelns andra sida: "))#Ber om ett värde på andra sidan

area=side1*side2#Räknar ut area
a = "-"
y = "|"
print(f"Rektangeln har sidorna {side1} och {side2} vilket gör att arean är {area}")

if side1 == side2:
    print("Eftersom bägge sidorna är lika långa så är denna rektangel en kvadrat.")
else:
    print("Eftersom sidorna är olika stora är denna en rektangel.")

#Denna kod skapar tabellen
print("Höjden | Volymen")
print(f"{a:-^17}")
for i in range (1, 11):
    b = i*25
    print("{0: >7} |{1: >7}".format(i,b))
