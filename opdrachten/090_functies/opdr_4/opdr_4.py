# Opdracht 1 functies
# Naam student: Elliot Kuster
# Groep:


def volledige_naam(lijst_met_namen):
    for naam in namen:
        if naam ["tussenvoegsel"]:
            print({naam['voornaam']},{naam['tussenvoegsel']},{naam['achternaam']})
        else: 
            print({naam['voornaam']},{naam['achternaam']})

namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)