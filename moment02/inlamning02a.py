#Moment02a med fördjupning

#importerar matte bibliotek
import math
math.pi
#Sätter pi som variabel för math.pi
pi=math.pi
#Skapar en input där programmet frågar om man vill använda heltal eller decimaler
meny=input("Vill du använda decimaler eller heltal som din radie?")

#Om man petar in heltal ovan blir radien en int (heltal), skriver man något annat blir det en float (Decimaler)
if meny == ("heltal"):
    radie=int(input("Vad är din radie?"))
else:
    radie=float(input("Vad är din radie"))

#Programmet räknar ut arean och omketsen
area=radie*radie*pi
omkrets=radie+radie*pi
#Programmet printar användarens givna radie och sedan skriver ut svaret med en avrundning på 2 decimaler
print(f"Din area av {radie} är {round (area,2)}")
print(f"Din Omkrets av {radie} är {round (omkrets,2)}")