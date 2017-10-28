"""
Ecrivez une suite d'instructions qui, à partir d'un nombre entier strictement positif saisi
par l'utilisateur, calcule et affiche la liste de ses diviseurs et leur nombre.
"""

nbr = 0
while nbr <= 0:
    nbr = int(input("Donnez un nombre entier > 0 : "))

for i in range(1, nbr):  # Pour chaque nombre entre 1 et le nombre choisi
    if nbr % i == 0:  # Si le nombre choisi est divisible par ce nombre
        print(i)
