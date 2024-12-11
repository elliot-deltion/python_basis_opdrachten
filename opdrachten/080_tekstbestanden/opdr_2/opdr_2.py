# Opdracht 2 tekstbestanden
# Naam student: Elliot Kuster
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....
active = True
keren = 1
while True:
    gok = int(input(prompt))
    if geheim_getal < gok:
        keren +=1
        print("lager")
        continue
    elif geheim_getal > gok:
        keren+=1
        print("hoger")
        continue
    else: active = False
    print(f"Hoera! het geraden getal is {geheim_getal} \n")
    print(f"je hebt het in {(keren)} gedaan")
    break