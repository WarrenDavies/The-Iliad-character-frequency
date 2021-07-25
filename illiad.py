import os

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
    'Aineias', \
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

books = os.listdir('./lang')
books = sorted(books)
print(books)

for character in characters:
    print(character + ',', end = '')
    for book in books:
        with open('./lang/' + book) as b:
            current_book = b.read()
        print(str(current_book.count(character)), end=',')
    print('')    

# for character in characters:
#     print(character + ': '  + str(book1.count(character)))
