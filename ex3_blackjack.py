from random import randint


def random_card():
    """
    Pick a random card
    :return: the value of the card
    """
    card = randint(1, 11)
    if card == 1:
        chosen = False
        while not chosen:
            value = input("Vous avez pioché un AS. 1 ou 11 ? ")
            if value == '1':
                card = 1
                chosen = True
            elif value == '11':
                card = 11
                chosen = True
    return card


card_value_player = 0
card_value_ia = 0

picked_card_player = random_card()
print("Vous avez pioché : %d" % picked_card_player)
card_value_player += picked_card_player

picked_card_ia = random_card()
print("L'ordinateur pioche...")
card_value_ia += picked_card_ia

picked_card_player = random_card()
print("Vous avez pioché : %d" % picked_card_player)
card_value_player += picked_card_player

if card_value_player == 21:
    print("Blackjack!")

new_card = card_value_player < 21
while new_card:
    answer = input("Voulez-vous une nouvelle carte? (carte/je reste)")
    if answer == 'carte':
        picked_card_player = random_card()
        print("Vous avez pioché : %d" % picked_card_player)
        card_value_player += picked_card_player

        if card_value_player > 21:
            print("Vous avez perdu! (> 21)")
            new_card = False
        elif card_value_player == 21:
            print("Vous avez atteint 21!")
            new_card = False
    elif answer == 'je reste':
        new_card = False
    else:
        print("Svp choisissez entre 'carte' et 'je reste'")

ia_new_card = 17 <= picked_card_ia == 21
while ia_new_card:
    card_value_ia += random_card()
    if card_value_ia > 21:
        print("Vous avez gagné! (IA > 21)")
    elif 17 <= card_value_ia <= 21:
        ia_new_card = False


if card_value_player > card_value_ia:
    print("Vous avez gagné!")
elif card_value_player < card_value_ia:
    print("Vous avez perdu!")
else:
    print("Egalité")
