"""
Ecologiste dans l'âme, vous êtes attentif au réchauffement climatique. Les températures élevées
de ce début d'automne vous étonnent. VOus souhaitez connaitre la moyenne des températures atteintes
ces 5, 10, 15 derniers jours. Ecrivez une suite d'instructions qui calcule la température moyenne
d'une série de valeurs saisie par l'utilisateur. Celui-ci saisira la valeur -100 pour marquer la
fin de l'encodage.
"""

temp_total = 0
nbr_tmp = 0
new_temp = True
while new_temp:
    temp_to_add = int(input("Quelle température voulez-vous ajouter? "))
    if temp_to_add == -100:
        new_temp = False
    else:
        nbr_tmp += 1
        temp_total += temp_to_add

print("Moyenne des températures  = %.1f" % (temp_total / nbr_tmp))
