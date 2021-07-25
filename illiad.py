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
    Character('Athene', "Deity", []), # Athena, Pallas Athene/a \
    Character('Aphrodite', "Deity", []), \
    Character('Poseidon', "Deity", []), \
    Character('Ares', "Deity", []), \
    Character('Hephaistos', "Deity", []), # Hephaestus \
    Character('Apollo', "Deity", []), \
    Character('Hermes', "Deity", []), \
    Character('Thetis', "Deity", []), \
    Character('Dawn', "Deity", []), # Eos \
    Character('Iris', "Deity", []), \

    # Greeks
    ########
    Character('Achilles', "Greek", []), \
    Character('Agamemnon', "Greek", []), \
    Character('Antilochus', "Greek", []), \
    Character('Aias', "Greek", []), # Ajax \ 
    Character('Calchas', "Greek", []), \
    Character('Diomedes', "Greek", []), \
    Character('Helen', "Greek", []), \
    Character('Idomeneus', "Greek", []), \
    Character('Menelaos', "Greek", []), # Menelaus \
    Character('Nestor', "Greek", []), \
    Character('Odysseus', "Greek", []), \
    Character('Patroklos', "Greek", []), \
    Character('Phoinix', "Greek", []), #Phoenix \
    Character('Teukros', "Greek", []), # Teucer, Teucros, Teucris, Teucris\
    Character('Aisymnos', "Greek", []), #Aesymnos, Aesymnus\

    # Trojans
    #########
    Character('Aineias', "Trojan", []), # Aeneas\
    Character('Agenor', "Trojan", []), \
    Character('Andromache', "Trojan", []), \
    Character('Antenor', "Trojan", []), \
    Character('Cassandra', "Trojan", []), \
    Character('Glaukos', "Trojan", []), # Glaucus \
    Character('Hector', "Trojan", []), \
    Character('Laodike', "Trojan", []), # Laodice\
    Character('Lykaon', "Trojan", []),  # Lycaon \
    Character('Pandaros', "Trojan", []), # Pandarus \
    Character('Paris', "Trojan", []),  \
    Character('Polydamas', "Trojan", []),  \
    Character('Priam', "Trojan", []),  \
    Character('Sarpedon', "Trojan", []),  \
    Character('Theano', "Trojan", []),  \
    Character('Briseis', "Trojan", []),  \
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
