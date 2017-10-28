"""
Première année à l'univsersité, vous êtes bien décidé à vous organiser et à ne pas
vous laisser dépasser... Quoi de mieux pour planifier votre travail qu'un calendrier.
Ecrivez une fonction affichant un calendrier (chiffré uniquement) pour un mois en particulier
ou pour l'année entière. Attention au nombre de jours variables par mois et aux années bissextiles.

Rappel : Les années multiples de 4 sont bissextiles, sauf les années multiples de 100 qui ne le sont
pas, sauf les années multiples de 400 qui le sont. Ainsi, 2200 n'est pas bissextiles, mais 2400 oui.
"""


def show_calender(year, month):
    """
    Show the calender for the month chosen
    :param year: the year you chose (int)
    :param month: the month you chose (int)
    """

    for i in range(1, nbr_days_in_month(year, month) + 1):
        print(i, end=" ")
        # Attribut 'end' pas obligatoire
        # Il permet d'éviter de retourner à la ligne à chaque print


def nbr_days_in_month(year, month):
    """
    Returns the number of days in the chosen month
    :param year: the year you chose (int)
    :param month: the month you chose (int)
    :return: number of days in month 'month' (int)
    """

    if month == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return 29
                else:
                    return 28
            else:
                return 29
        else:
            return 28
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    else:
        return 30


show_calender(2018, 5)
