#Uppgift: m02u02
import math

a = 9
b = 2
f = 4.0
namn = "Oscar"

svar1 = a*b
svar2 = a*f
svar3 = a/b
svar4 = a // b
svar5 = a % b
svar6 = a ** 0.5
svar7 = b*b
svar8 = f*f
svar9 = a =+ b

print(svar1)
print(svar2)
print(svar3)
print(namn)
print(svar4)
# Heltalsdivisionen mellan a och b blir 4
print(svar5)
# Resten mellan a och b blir 1
print(svar6)
# Roten ur a blir 3.0
print(svar7)
# Kvadraten av b blir 4
print(svar8)
# Kvadraten av f blir 16.0

print(type (svar1))
print(type (svar2))
print(type (namn))
print(type (svar4))
# Det blir en int då det ej finns decimaler
print(type (svar5))
# Det blir en int då det ej finns decimaler
print(type (svar6))
# Det blir en float då det finns decimaler
print(type (svar7))
# Det blir en int då det ej finns decimaler
print(type (svar8))
#Det blir en float då det finns decimaler