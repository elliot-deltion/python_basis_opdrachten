# Opdracht 3 Tekst opslaan
# Naam student: Elliot Kuster
# Groep:

tekst = input("Geef de tekst die wilt encrypten: \n")
tekst_encrypted = ""

for teken in tekst:
    if teken == " ":
        tekst_encrypted += " "
    elif teken == ",":
        tekst_encrypted += ","
    elif "a" <= teken <= "z":
        tekst_code = ord(teken) - ord("a")
        tekst_code_encrypted = (tekst_code+5) % 26
        tekst_encrypted += chr(tekst_code_encrypted + ord("a"))
    else: 
        "A" <= teken <= "Z"
        tekst_code = ord(teken) - ord("A")
        tekst_code_encrypted = (tekst_code+5) % 26
        tekst_encrypted += chr(tekst_code_encrypted + ord("A"))

print(tekst_encrypted)