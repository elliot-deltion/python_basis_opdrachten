# Opdracht 2 lists
# Naam student: Elliot Kuster
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....
print(rivieren[0])
print(f"De rivier {rivieren[0].title()} onder andere door {rivier_info['rijn'][1].title()}")

print(rivieren[1])
print(f"De rivier {rivieren[0].title()} onder andere door {rivier_info['rijn'][0].title()}")

print(rivieren[2])
print(f"De rivier {rivieren[2].title()} onder andere door {rivier_info['nijl'][2].title()}")