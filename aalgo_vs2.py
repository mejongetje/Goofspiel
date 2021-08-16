from functools import singledispatch
import random


weights = [[0, .4144, .0897, .4959, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, .2266, .0216, .2991, .0976, .3551, 0, 0, 0, 0, 0, 0, 0],
         [.519, 0, .1784, .0340, .2301, .0929, .2740, .1386, 0, 0, 0, 0, 0],
         [.0309, .0204, .0952, .0610, .1343, .1073, .1754, .1544, .2210, 0, 0, 0, 0],
         [0, 0.558, .0357, .0873, .0667, .1242, .1014, .1654, .1481, .2155, 0, 0, 0],
         [0, .0727, .0025, .0985, 0, .1846, .0018, .2184, .0451, .2664, .1100, 0, 0],
         [0, 0, .0694, 0, .1237, 0, .1675, .0209, .2021, 0, .3967, 0, 0],
         [0, .0338, .0215, .0536, .0395, .0767, .0602, .1028, .0917, .1436, .1506, .2262, 0],
         [0, .0473, .0015, .0648, 0, .1198, .0012, .1422, .0295, .1766, 0, .4171, 0],
         [0, .0361, 0, .0673, 0, .0985, 0, .1384, .0151, .1696, .0635, .2410, .1704],
         [.0145, .0, .0410, 0, .0803, 0, .1016, .0156, .1229, 0, .2530, .0228, .3482],
         [0, .0304, .0, .0561, .0, .0819, .0080, .0987, .0280, .1243, .0646, 0, .5081],
         [.0100, 0, .0370, 0, .0655, 0, .0875, 0, .1262, .1288, 0, 0, .6610]]


def prizeisone(weights):
    return random.choices(range(1,14), weights)

def prizeistwo(weights):
    return random.choices(range(1,14), weights)

def prizeisthree(weights):
    return random.choices(range(1,14), weights)

def prizeisfour(weights):
    return random.choices(range(1,14), weights)

def prizeisfive(weights):
    return random.choices(range(1,14), weights)

def prizeissix(weights):
    return random.choices(range(1,14), weights)

def prizeisseven(weights):
    return random.choices(range(1,14), weights)

def prizeiseight(weights):
    return random.choices(range(1,14), weights)

def prizeisnine(weights):
    return random.choices(range(1,14), weights)

def prizeisten(weights):
    return random.choices(range(1,14), weights)

def prizeiseleven(weights):
    return random.choices(range(1,14), weights)

def prizeistwelve(weights):
    return random.choices(range(1,14), weights)

def prizeisthirteen(weights):
    return random.choices(range(1,14), weights)


def check_hand(prize, hand1, hand2, weights=weights):
    full_hand = [x for x in range(1,14)]  # list with numbers from 1 to 13
    hand1_ranks = [card.rank for card in hand1] # list with ranks in the hand
    rank_in_hand = [] # list with ranks and zeros, where rank is not in the hand
    for el in full_hand:
        if el in hand1_ranks:
            rank_in_hand.append(el)
        else:
            rank_in_hand.append(0)
    amended_weights = []    # list with weights for specific ranks in rank_in hand and zeros for ranks not in hand and zeros for ranks not weighted
    for el in rank_in_hand:
        if el:
            amended_weights.append(weights[full_hand.index(prize.rank)][rank_in_hand.index(el)])
        else:
            amended_weights.append(0)
    if sum(amended_weights):
        return use_dispatch(hand1, prize, amended_weights)
    else:
        print('NOTFALL')
        return use_other(hand1, hand2)


def use_dispatch(hand1, prize, weights):

    dispatch = {
        1: prizeisone(weights),
        2: prizeistwo(weights),
        3: prizeisthree(weights),
        4: prizeisfour(weights),
        5: prizeisfive(weights),
        6: prizeissix(weights),
        7: prizeisseven(weights),
        8: prizeiseight(weights),
        9: prizeisnine(weights),
        10: prizeisten(weights),
        11: prizeiseleven(weights),
        12: prizeistwelve(weights),
        13: prizeisthirteen(weights)
          }

    card_rank = dispatch[prize.rank]
    play_card = [card for card in hand1 if card.rank == card_rank[0]]
    return play_card[0]


def use_other(hand1, hand2):
    hand1_sum = sum([card.rank for card in hand1])
    hand2_sum = sum([card.rank for card in hand2])
    if hand1_sum > hand2_sum:
        return hand1[-1]
    else:
        return hand1[0]
