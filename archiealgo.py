import random

# Computer algo

def archie_bid(prize, player, gamestock):
    option = random.randint(0,4)
    ranks = [card.rank for card in player.hand]
    length = len(player.hand)
    sum_game_stock = sum([card.rank for card in gamestock])
    if sum_game_stock > 13:
        card = player.hand[-1]
        return card
    elif option == 0:
        if prize.rank in ranks:
            card = next(card for card in player.hand if card.rank == prize.rank)
            return card
        elif (prize.rank + 1) in ranks:
            card = next(card for card in player.hand if card.rank == prize.rank + 1)
            return card
        elif (prize.rank - 5) in ranks:
            card = next(card for card in player.hand if card.rank == prize.rank - 5)
            return card
        else:
            return player.hand[0]
    elif option == 1:
        if  prize.rank in ranks:
            card = next(card for card in player.hand if card.rank == prize.rank)
            return card
        elif (prize.rank + 1) in ranks:
            card = next(card for card in player.hand if card.rank == prize.rank + 1)
            return card
        else:
            return player.hand[0]
    elif option == 2:
        if  prize.rank in ranks:
            card = next(card for card in player.hand if card.rank == prize.rank)
            return card
        elif (prize.rank - 6) in ranks:
            card = next(card for card in player.hand if card.rank == prize.rank - 6)
            return card
        else:
            return player.hand[0]
    else: 
        if prize.rank < 9:
            return player.hand[random.randint(0,length-1)]
        else:
            return player.hand[-1]
