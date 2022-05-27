from random import choice


def continue_game():
    print('Do you want to play again?')
    answer = input()
    while answer not in ('yes', 'no'):
        answer = input('Write please yes or no')
    if answer == 'yes':
        game()
    else:
        print('See you again!')



def game():
    var = (1, 2)
    box_1 = []
    box_2 = []
    players = {player_1: box_1, player_2: box_2}
    chance = choice(var)
    if chance == 1:
        box_1.append('carrot')
    else:
        box_2.append('carrot')
    print(player_1, ', are you ready to look in your box? yes or no')
    while True:
        answer = input()
        if answer == 'yes':
            print(box_1)
            break
        elif answer == 'no':
            print('Then think a little else')
        else:
            print('Write please yes or no')
    print(player_1, ', is there the carrot in your box?')
    print(input())
    print(player_2, ', do you want to exchange your box with ', player_1, '?')
    while True:
        answer = input()
        if answer == 'yes':
            print(f'Then your box is {box_1}, and the {player_1} box is {box_2}')
            players[player_1], players[player_2] = box_2, box_1
            break
        elif answer == 'no':
            print('Then you both ara remaining with your boxes')
            break
        else:
            print('Write please yes or no')
    print('So, now we will know in which box the carrot is...')
    print(players[player_1])
    print(players[player_2])



# hello
print("Hello! You came in the game 'Carrot in the box'. And here are the rules: ... rules ...")

print('First player, write your name')
player_1 = input()
print('Second player, write your name')
player_2 = input()
