import os #, pandas as pd

class character:
    def __init__(name, group, counts):
        self.name = name
        self.group = group
        self.counts = []

characters = [ \

    # Deities
    #########
    'Zeus', \
    'Hera', \
    'Athene', \
    'Aphrodite', \
    'Poseidon', \
    'Ares', \
    # 'Hephaestus', \
    'Hephaistos', \
    'Apollo', \
    # 'Hermes', \
    # 'Thetis', \

    # Greeks
    ########
    'Achilles', \
    'Agamemnon', \
    # 'Antilochus', \
    #'Ajax the greater', # not used in Lang \
    #'Ajax the Lesser', # not used in Lang \
    'Aias', # Lang spelling of Ajax \ 
    # 'Antilochus', \
    # 'Calchas', \
    # 'Diomedes', \
    'Helen', \
    # 'Idomeneus', \
    # 'Menelaus', \ # not used in Lang 
    'Menelaos', \
    'Nestor', \
    'Odysseus', \
    'Patroklos', \
    # 'Phoenix', \
    # 'Teucer', \
    # 'Aesymnus', \

    # Trojans
    #########
    # 'Aeneas', \ # not used in Lang 
    # 'Aineias', \ 
    # 'Agenor', \
    # 'Andromache', \
    # 'Antenor', \
    # 'Cassandra', \
    # 'Glaucus', \
    'Hector', \
    # 'Laodice', \
    # 'Lycaon', \
    # 'Pandarus', \
    'Paris', \
    # 'Polydamas', \
    'Priam', \
    # 'Sarpedon', \
    # 'Theano', \
    # 'Briseis', \
]

counts = []
for character in characters:
    counts.append([character])

books = os.listdir('./lang')
books = sorted(books)
print(books)


for book in books:
    with open('./lang/' + book) as b:
        current_book = b.read()
    i = 0
    for character in characters:
        counts[i].append(current_book.count(character))   
        i = i + 1

for character in counts:
    for count in character:
        print(str(count) + ",", end='')
    print('')