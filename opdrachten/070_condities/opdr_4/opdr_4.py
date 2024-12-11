# Opdracht 4 condities
# Naam student: Elliot Kuster
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]

# Hier de rest van jouw code...
beschikbare_toppings = []
kosten = []
for topping in toppings:
    beschikbare_toppings.append(topping[0])
    kosten.append(topping[1])

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")
if keuze in beschikbare_toppings:
    index = beschikbare_toppings.index(keuze)
    prijs = kosten[index]
    print(f"U heeft {keuze} besteld. Dat kost {prijs}")
else:
    print("Uw keuze zit niet in ons assortiment")