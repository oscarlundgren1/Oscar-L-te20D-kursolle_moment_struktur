#En input som frågar om ett värde
salary = int(input("Vad är din bruttolön i kr varje månad? "))

#variablar/olika typer av skatt i decimalform
Municipal_tax = 0.2136
County_council_tax = 0.1148

print("\n")

print("Utskrift")
print(f"Månadslön : {salary}kr")#Printar månadslönen med hjälp av inputen ovan
print(f"Kommunal Skatt : {round(Municipal_tax * salary)}kr")#Printar hur mycket kommunal skatt, multiplicera skatt med lönen
print(f"Lanstingsskatt : {round(County_council_tax * salary)}kr")#Printar hur mycket Lanstingsskatt, multiplicera skatt med lönen
local_month_tax = salary * County_council_tax#Variabel, lönen multiplicerat med skatt
kom_month_tax = salary * Municipal_tax#Variabel, lönen multiplicerat med skatt
print(f"Kvar efter skatt : {round(salary - local_month_tax - kom_month_tax)}kr")#Printar vad som finns kvar av lönen efter skatten