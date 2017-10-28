"""
Ecrivez une suite d'instructions qui, étant donné une série d'entiers positifs saisie au clavier
(-1 marquant la fin de la série et ne faisant pas partie de la série), affiche le nombre de fois
où le minimum et le maximum de cette série y figurent.

Exemple : Dans la suite 12 12 34 45 45 12, le minimum y figure 3 fois et le maximum, 2 fois.
"""

current_max = -1  # Ne fais pas partie de la série, on aura jamais -1 en max
nbr_max = 0  # Nombre d'occurences du nombre max

current_min = -1  # Ne fais pas partie de la série, on aura jamais -1 en min
nbr_min = 0  # Nombre d'occurences du nombre min

new_number = True
while new_number:  # Boucle infinie jusqu'à ce qu'on mette '-1'
    number = int(input("Quelle nombre voulez-vous ajouter? > "))
    if number == -1:  # Condition qui check si on veut arrêter la boucle
        new_number = False
    else:
        if number < current_min or current_min == -1:
            # On regarde si le nombre ajouté est plus petit que le minimum actuel
            # ou que le minimum actuel = -1 -> d'office le min alors
            current_min = number
            nbr_min = 1
        elif number == current_min:
            nbr_min += 1

        if number > current_max or current_max == -1:
            # On regarde si le nombre ajouté est plus grand que le max actuel
            # ou que le max actuel = -1 -> d'office le max alors
            current_max = number
            nbr_max = 1
        elif number == current_max:
            nbr_max += 1

print('Maximum:')
print(current_max)
print(nbr_max)
print('----')
print('Minimum:')
print(current_min)
print(nbr_min)
