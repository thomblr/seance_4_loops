"""
Vous n'êtes pas spécialement radin... mais vous aimez quand même l'argent que vous placez
en banque vous rapporte. Votre objectif est fixé : après vos études, vous partez aux USA.
Pour constituer votre bas de laine, vous souhaitez faire un placement. Vous souhaitez faire
quelques simulations avant de faire votre choix parmi les offres de votre banquier.

(a) Implémentez une fonction qui, étant donné un capital placé et un taux d'intérêt annuel,
retourne la valeur totale acquise après un an de placement.

(b) Généralisez cette fonction afin qu'elle donne le rendement d'un placement après x années.
"""


def placement_value(capital, rate):
    """
    Returns the value of a placement based on a specific rate during a year
    :param capital: the money you have (float)
    :param rate: the rate of the placement (float)
    :return: the value after a year (float)
    """

    return capital * (1 + rate)


def placement_value_after_x_year(capital, rate, year):
    """
    Returns the value of a placement after x years
    :param capital: the money you have (float)
    :param rate: the rate of the placement (float)
    :param year: how long the placement lasts (int)
    :return: the value after x year (float)
    """

    value = capital
    for i in range(1, year + 1):
        value += value * rate
    return value


print(placement_value(1000000, 0.05))
print(placement_value_after_x_year(1000000, 0.05, 2))
print(placement_value_after_x_year(100, 0.05, 100))
