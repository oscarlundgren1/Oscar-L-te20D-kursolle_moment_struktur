#Mycket av denna kod är samma som föregående
salary = int(input("Vad är din bruttolön i kr varje månad? "))

Municipal_tax = 0.2136
County_council_tax = 0.1148
breakingpoint_tax = 0.2
protection_tax = 0.05

if salary > 1604 and salary < 39058:
    print("\n")

    print("Utskrift")
    print(f"Månadslön : {salary}kr (Årslön: {salary*12})")
    print(f"Kommunal Skatt : {round(Municipal_tax * salary)}kr")
    print(f"Lanstingsskatt : {round(County_council_tax * salary)}kr")
    local_month_tax = salary * County_council_tax
    kom_month_tax = salary * Municipal_tax
    total_tax = local_month_tax + kom_month_tax#Räknar ut total skatt i kr
    total_per = Municipal_tax + County_council_tax#Räknar ut totala skatt i %
    #total_tax = salary * Municipal_tax * County_council_tax
    print(f"Kvar efter skatt : {round(salary - local_month_tax - kom_month_tax)}kr")
    print(f"Total skatt: {round(total_tax)}Kr")
    print(f"Andel betald skatt: {round(total_per * 100)} %")#Multiplicerar total % med 100 för att få i % form

elif salary > 39058 and salary < 56308:
    print("\n")

    print("Utskrift")
    print(f"Månadslön : {salary}kr (Årslön: {salary*12})")
    print(f"Kommunal Skatt : {round(Municipal_tax * salary)}kr")
    print(f"Lanstingsskatt : {round(County_council_tax * salary)}kr")
    print(f"Statlig skatt : {round(breakingpoint_tax * salary)}kr")
    local_month_tax = salary * County_council_tax
    kom_month_tax = salary * Municipal_tax
    state_tax = salary * breakingpoint_tax
    total_tax = local_month_tax + kom_month_tax + state_tax
    total_per = Municipal_tax + County_council_tax + breakingpoint_tax
    print(f"Kvar efter skatt : {round(salary - local_month_tax - kom_month_tax - state_tax)}kr")
    print(f"Total skatt: {round(total_tax)}")
    print(f"Andel betald skatt: {round(total_per * 100)} %")

elif salary > 56308:
    print("\n")

    print("Utskrift")
    print(f"Månadslön : {salary}kr (Årslön: {salary*12})")
    print(f"Kommunal Skatt : {round(Municipal_tax * salary)}kr")
    print(f"Lanstingsskatt : {round(County_council_tax * salary)}kr")
    print(f"Statlig skatt : {round(salary * breakingpoint_tax * protection_tax)}kr")
    local_month_tax = salary * County_council_tax
    kom_month_tax = salary * Municipal_tax
    state_tax_max = salary * breakingpoint_tax * protection_tax
    total_tax = local_month_tax + kom_month_tax + state_tax_max
    total_per = Municipal_tax + County_council_tax + protection_tax + breakingpoint_tax
    print(f"Kvar efter skatt : {round(salary - local_month_tax - kom_month_tax - state_tax_max)}kr")
    print(f"Total skatt: {round(total_tax)}")
    print(f"Andel betald skatt: {round(total_per * 100)} %")
else:
    print("\n")

    print("Utskrift")
    print(f"Månadslön : {salary}kr (Årslön: {salary*12})")
    print(f"Kvar efter skatt : {round(salary)}kr")
    print("Eftersom du tjänar under brytpunkten betalar du ingen skatt")