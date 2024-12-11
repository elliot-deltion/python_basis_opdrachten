# Opdracht 1 while-loops
# Naam student: Elliot Kuster
# Groep:

# Jouw code komt hier
vraag1 = 'Wat vind je van de huidige regering?'
vraag2 = 'Wat vind je van de Python-lessen tot nu toe?'
vraag3 = 'Wat vind jij de mooiste stad van Nederland?'

active = True
enquete = []
while active:
    message = input(f"{vraag1}\n")
    message2 = input(f"{vraag2}\n")
    message3 = input(f"{vraag3}\n")
    if message == 'q':
        active = False
        fo = open('newtext.txt', 'wt')
        for antwoord in enquete:
            fo.write(antwoord + "\n")
        fo.close()
    else:
        enquete.append(message)
        enquete.append(message2)
        enquete.append(message3)
