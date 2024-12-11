# Opdracht 3 condities
# Naam student: Elliot Kuster
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...
leeftijd = int(input("Geef uw leeftijd in aantal jaar\n"))
if leeftijd <=2:
    print("Baby's t/m 2 mogen gratis!")
elif leeftijd >2 and leeftijd <=18:
    print("U behoort tot de groep kinderen\n","U krijgt 50% korting\n","U betaalt daarom",normale_toegangsprijs/2)
elif leeftijd >18 and leeftijd <=64:
    print("U behoort tot de groep volwassenen\n U krijgt 0% korting\n U betaalt daarom",normale_toegangsprijs)
elif leeftijd >64 and leeftijd <=150:
    print("U behoort tot de groep ouderen\n U krijgt 30% korting\n U betaalt daarom",12.50-(normale_toegangsprijs*0.3))