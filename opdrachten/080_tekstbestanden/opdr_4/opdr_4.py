# Opdracht 4 Tekst opslaan
# Naam student: Elliot Kuster
# Groep:


# Party enquete
vraag1 = "Wat is je voornaam?"
vraag2 = "Wat is je achternaam?"
vraag3 = "Wat neem je mee aan drank?"
vraag4 = "Wat neem je mee om te eten?"

active = True
feestje = []
nummer = 0
while active:
        antwoord1 = input(f"{nummer+1}. {vraag1}\n")
        antwoord2 = input(f"{nummer+2}. {vraag2}\n")
        antwoord3 = input(f"{nummer+3}. {vraag3}\n")
        antwoord4 = input(f"{nummer+4}. {vraag4}\n")
        if antwoord1 == 'q':
                active = False
                fo = open('enquete.txt', 'at')
                for answer in feestje:
                    fo.write(f"{answer}\n")
                fo.close()
        else: lijstje = {'naam':antwoord1,'achternaam':antwoord2,'drank':antwoord3,'eten':antwoord4}
        feestje.append(lijstje)
        print("Bedankt voor het invullen! \nSee you at the party!")