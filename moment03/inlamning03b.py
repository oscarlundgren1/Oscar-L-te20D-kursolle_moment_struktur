#Mycket av denna kod är samma som föregående
salary = int(input("Vad är din bruttolön i kr varje månad? "))

Municipal_tax = 0.2136
County_council_tax = 0.1148

#Lagt till en if sats då jag har flera villkår
if salary > 1604:#Om lönen är större än 1604 körs denna kod
    print("\n")

    print("Utskrift")
    print(f"Månadslön : {salary}kr")
    print(f"Kommunal Skatt : {round(Municipal_tax * salary)}kr")
    print(f"Lanstingsskatt : {round(County_council_tax * salary)}kr")
    local_month_tax = salary * County_council_tax
    kom_month_tax = salary * Municipal_tax
    print(f"Kvar efter skatt : {round(salary - local_month_tax - kom_month_tax)}kr")
else:#Om inte villkåret ovan gäller körs denna
    print("\n")

    print("Utskrift")
    print(f"Månadslön : {salary}kr (Årslön: {salary*12})")
    print(f"Kvar efter skatt : {round(salary)}kr")
    print("Eftersom du tjänar under brytpunkten betalar du ingen skatt")