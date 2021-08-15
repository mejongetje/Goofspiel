import random

from os import name, system


def print_hand(player):
    i = 1
    strng = ' '
    for card in player.hand:
        strng += '['+str(i)+']'+ card.name + ' '
        i += 1
        if len(strng) >= 45 and len(strng) < 50:
            strng += ' |\n|\n| '
    return strng 


def bid_card(hu_inp, player):
    card = player.hand.pop(hu_inp - 1)
    return card


def winning_card(card_p1, card_p2, card, game_stock):
    if card_p1.rank > card_p2.rank:
        return card_p1
    elif card_p2.rank > card_p1.rank:
        return card_p2
    else:
        game_stock.append(card)
        return None


def prize_winner(card, players):
    if card == None:
        return None        
    elif card.suit == 2:
        return players[0]
    else:
        return players[1]


def add_points(prize, winner, game_stock):
    stock_points = sum([card.rank for card in game_stock])
    points = prize.rank + stock_points
    winner.points += points
    return points


def round_up(prize, winner, win_card, game_stock):
    points = add_points(prize, winner, game_stock)
    print(f'{winner} had the highest bid with {win_card}...')
    print(f'...and adds {points} to his total.')


def hand_result(players):
    if players[0].points >= players[1].points:
        return players[0]
    else:
        return players[1]


def clear():  
    if name == 'nt':
        system('cls') 
    else:
        system('clear')