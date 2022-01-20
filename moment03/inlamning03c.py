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
    print(f"Kvar efter skatt : {round(salary - local_month_tax - kom_month_tax)}kr")

elif salary > 39058 and salary < 56308:
    print("\n")

    print("Utskrift")
    print(f"Månadslön : {salary}kr (Årslön: {salary*12})")
    print(f"Kommunal Skatt : {round(Municipal_tax * salary)}kr")
    print(f"Lanstingsskatt : {round(County_council_tax * salary)}kr")
    print(f"Statlig skatt : {round(salary * breakingpoint_tax)}kr")
    local_month_tax = salary * County_council_tax
    kom_month_tax = salary * Municipal_tax
    state_tax = salary * breakingpoint_tax
    print(f"Kvar efter skatt : {round(salary - local_month_tax - kom_month_tax - state_tax)}kr")

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
    print(f"Kvar efter skatt : {round(salary - local_month_tax - kom_month_tax - state_tax_max)}kr")
else:
    print("\n")

    print("Utskrift")
    print(f"Månadslön : {salary}kr (Årslön: {salary*12})")
    print(f"Kvar efter skatt : {round(salary)}kr")
    print("Eftersom du tjänar under brytpunkten betalar du ingen skatt")