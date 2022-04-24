from random import randint


def welcome():  # приветствие
    print('''I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:''')
    print('''When I say: That means:
Pico: One digit is correct but in the wrong position.
Fermi: One digit is correct and in the right position.
Bagels: No digit is correct.''')


def game():  # собственно, сама игра
    number = str(randint(100, 999))  # генерируем случайное число из диапазона (100, 999) и переводим в строку
    print('I have thought a number!')
    attempt = input('Write a number. Try to guess!')  # игрок вводит число
    while not attempt.isdigit() and len(attempt) != 3:
        attempt = input('Incorrect answer. Try again!')
    if attempt == number:
        print('You got it!')
        continue_game()
    for i in attempt:
        if i in number:
            pass


def continue_game():  # предложение сыграть ещё раз...
    pass
