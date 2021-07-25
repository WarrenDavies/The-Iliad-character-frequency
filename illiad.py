import os #, pandas as pd

class Character:
    def __init__(self, name, group, counts):
      self.name = name
      self.group = group
      self.counts = counts

characters = [ \
    # Deities
    #########
    Character('Zeus', "Deity", []), \
    Character('Hera', "Deity", []), \
    Character('Athene', "Deity", []), \
    Character('Aphrodite', "Deity", []), \
    Character('Poseidon', "Deity", []), \
    Character('Ares', "Deity", []), \
    # Character('Hephaestus', "Deity", []), \
    Character('Hephaistos', "Deity", []), \
    Character('Apollo', "Deity", []), \
    # Character('Hermes', "Deity", []), \
    # Character('Thetis', "Deity", []), \

    # Greeks
    ########
    Character('Achilles', "Greek", []), \
    Character('Agamemnon', "Greek", []), \
    #Character('Antilochus', "Greek", []), \
    #Character('Ajax the greater', "Greek", []), # not used in Lang \
    #Character('Ajax the Lesser', "Greek", []), # not used in Lang \
    Character('Aias', "Greek", []), # Lang spelling of Ajax \ 
    # Character('Antilochus', "Greek", []), \
    # Character('Calchas', "Greek", []), \
    # Character('Diomedes', "Greek", []), \
    Character('Helen', "Greek", []), \
    # Character('Idomeneus', "Greek", []), \
    # Character('Menelaus', "Greek", []), \ # not used in Lang 
    Character('Menelaos', "Greek", []), \
    Character('Nestor', "Greek", []), \
    Character('Odysseus', "Greek", []), \
    Character('Patroklos', "Greek", []), \
    # Character('Phoenix', "Greek", []), \
    # Character('Teucer', "Greek", []), \
    # Character('Aesymnus', "Greek", []), \

    # Trojans
    #########
    # Character('Aeneas', "Trojan", []), \ # not used in Lang 
    # Character('Aineias', "Trojan", []), \ 
    # Character('Agenor', "Trojan", []), \
    # Character('Andromache', "Trojan", []), \
    # Character('Antenor', "Trojan", []), \
    # Character('Cassandra', "Trojan", []), \
    # Character('Glaucus', "Trojan", []), \
    Character('Hector', "Trojan", []), \
    # Character('Laodice', "Trojan", []),  \
    # Character('Lycaon', "Trojan", []),  \
    # Character('Pandarus', "Trojan", []),  \
    Character('Paris', "Trojan", []),  \
    # Character('Polydamas', "Trojan", []),  \
    Character('Priam', "Trojan", []),  \
    # Character('Sarpedon', "Trojan", []),  \
    # Character('Theano', "Trojan", []),  \
    # Character('Briseis', "Trojan", []),  \
]

books = os.listdir('./lang')
books = sorted(books)

for book in books:
    with open('./lang/' + book) as b:
        current_book = b.read()
    for character in characters:
        character.counts.append(current_book.count(character.name))   

for character in characters:
    print(character.name + ',' + character.group + ',', end='')
    for count in character.counts:
        print(str(count) + ",", end='')
    print('')
