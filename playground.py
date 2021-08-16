import os

import archiealgo
import aalgo_vs2
import classes
import headers
import utils


utils.clear()
headers.archie()
inp = input('Enter to challenge Archie for a game of Goofspiel.'.center(65))
utils.clear()

while True:

    game = classes.Board()
    classes.p1.hand = game.clubs
    classes.p2.hand = game.spades
    prize_pile = game.diamonds
    classes.p1.points, classes.p2.points = 0, 0
    repeat = 1

    while game.diamonds:

        hand_strng = utils.print_hand(classes.p2)

        headers.header()
        print('|                   A R C H I E                    |')
        print('|--------------------------------------------------|')
        print('|                        ----                      |')
        print(f'|   {str(classes.p1.points).center(4)}points          | {classes.p1.card} |         PRIZE CARD  |')
        print('|                        ----            ******    |')
        print(f'|                                        * {prize_pile[0]} *    |')
        print('|                        ----            ******    |')
        print(f'|   {str(classes.p2.points).center(4)}points          | {classes.p2.card} |                     |')
        print('|                        ----                      |')
        print('|--------------------------------------------------|')
        print(f'|{hand_strng}')
        print('----------------------------------------------------')
        print('----------------------------------------------------')
        
        if repeat == 1:
            while True:
                try:
                    hu_inp = int(input('Select a card for your bid. '.center(52)))
                    if hu_inp <= len(classes.p2.hand):
                        break
                except:
                    pass
            classes.p2.card = utils.bid_card(hu_inp, classes.p2)
            classes.p1.card = aalgo_vs2.check_hand(prize_pile[0], classes.p1.hand, classes.p2.hand)
            classes.p1.hand.remove(classes.p1.card)
            
        
        # Reveal the bidding cards:    
        elif repeat == 2:

            print(f'You bid the {classes.p2.card}')
            print(f'Archie bids the {classes.p1.card}')
            win_card = utils.winning_card(classes.p1.card, classes.p2.card, prize_pile[0], game.stock)
            if win_card == None:
                print('We have a draw! Prize moves to next round.')
                repeat += 1
            winner = utils.prize_winner(win_card, classes.Player.players)
            classes.p1.card = '  '
            classes.p2.card = '  '
            prize = prize_pile.pop(0)
            inp3 = input('Click enter to continue.'.center(52))


        # Compare the bidding cards
        elif repeat == 3:
            utils.round_up(prize, winner, win_card, game.stock)            
            game.stock.clear()
            inp1 = input('Click enter to continue. '.center(52))
       
        repeat += 1

        if repeat == 4:
            repeat = 1

        if not game.diamonds:
                utils.round_up(prize, winner, win_card, game.stock)
                print('-------------------------------------------')
                hand_winner = utils.hand_result(classes.Player.players)
                print(f'{hand_winner} won this game with {hand_winner.points} points.')
                inp6 = input('Click enter to continue '.center(52))
                hand_winner.games_won += 1

        utils.clear()

    headers.header()
    print('|                      SCOREBOARD                  |')
    print('|--------------------------------------------------|')
    print('|                                                  |')
    print(f'|          You have beaten Archie {classes.p2.games_won} times.         |'.center(52))
    print('|                                                  |')
    print(f'|          Archie has beaten you {classes.p1.games_won} times.          |'.center(52))    
    print('|                                                  |')
    print('|--------------------------------------------------|')
    headers.footer()
    inpf = input('Do you want to continue playing? y or n  '.center(52))
    
    if inpf == 'n':
        break
    else:
        pass

    utils.clear()

