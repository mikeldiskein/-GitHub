from random import randint


def welcome():  # приветствие, правила
    print('''I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:''')
    print('''When I say: That means:
Pico: One digit is correct but in the wrong position.
Fermi: One digit is correct and in the right position.
Bagels: No digit is correct.''')


def continue_game():  # предложение сыграть ещё раз...
    answer = input('Would you like to play again? yes or no').lower()
    if answer == 'yes':
        return True
    elif answer == 'no':
        print('Goodbye! See you!')
        return False


def game():  # собственно, сама игра
    number = str(randint(100, 999))  # генерируем случайное число из диапазона (100, 999) и переводим в строку
    tries = 10  # количество попыток
    print('I have thought a number!')
    while tries > 0:
        attempt = input('Write a number. Try to guess!')  # игрок вводит число
        while not attempt.isdigit() and len(attempt) != 3:
            attempt = input('Incorrect answer. Try again!')
        tries -= 1
        if attempt != number:
            flag = True
            for i in attempt:
                if i in number:
                    if attempt.find(i) == number.find(i):
                        print("Fermi", end=' ')
                    elif attempt.find(i) != number.find(i):
                        print('Pico', end=' ')
                else:
                    flag = False
            if not flag:
                print('Bagels')
        elif attempt == number:
            print('You got it!')
            break
    if tries == 0:
        print('You lose...')
    if continue_game():
        game()


game()


