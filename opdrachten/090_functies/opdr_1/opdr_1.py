# Opdracht 1 functies
# Naam student: Elliot Kuster
# Groep:


def write_to_file(afile, atext):
    with open(afile, 'at') as file:
        file.write(atext + '\n')

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)
