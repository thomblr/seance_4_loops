def tchacatchac(vitesse):
    """
    Returns the time the train run over you
    :param vitesse: speed of the train
    :return: time of death
    """

    h = 9
    m = 0
    vitesse = vitesse / 3.6  # km/h -> m/s
    distance = 170000  # 170 km
    time = distance / vitesse  # en sec
    ho = time // 3600
    mi = (time // 60) % 60
    h += ho
    m += mi
    return "%d:%d" % (int(h), int(m))


for i in range(100, 300, 10):
    print(tchacatchac(i))
