from random import randint

"""
Fan de devinettes, vous écrivez une suite d'instructions correspondant au jeu, illustré
ci-dessous, qui consiste à deviner un nombre entre 1 et 100, en 10 coups maximum.
"""

random_number = randint(1, 101)
print("Trouvez un nombre entre 1 et 100:")

found = False
nbr_looked = 0
while not found:
    if nbr_looked == 10:
        found = True
        print("You lost!")
    else:
        value = int(input("> "))
        print(value)
        nbr_looked += 1
        if value < random_number:
            print("Too small!")
        elif value > random_number:
            print("Too large!")
        else:
            print("Vous avez trouvé le nombre en %d coups!" % nbr_looked)
            found = True
