from random import *

word_list = ['КОСМОС', 'ДЫРА', 'СВЕРХНОВАЯ', 'АСТЕРОИД', 'КОМЕТА', 'ПЛАНЕТА', 'ЗВЕЗДА', 'ГАЛАКТИКА', 'СОЛНЦЕ', 'ЛУНА',
             'МАРС', 'ВЕНЕРА', 'МЕРКУРИЙ', 'КЛАСТЕР', 'КРАТЕР', 'ВЗРЫВ', 'МАТЕРИЯ', 'ЭНЕРГИЯ', 'ЧАСТИЦЫ', 'ИЗЛУЧЕНИЕ']


def get_word():
    return choice(word_list).upper()


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # голова, торс, обе руки, одна нога
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        # голова, торс, обе руки
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        # голова, торс и одна рука
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        # голова и торс
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        # голова
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def continue_game():
    print("Быть может, ты хочешь сыграть ещё раз?")
    while True:
        if input().upper() == "ДА":
            return True
        elif input().upper() == "НЕТ":
            return False
        else:
            print("Ответь 'да' или 'нет'")
            continue


def play(word):
    word = get_word()
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = ''
    guessed_words = ''
    tries = 6
    print("Давайте играть в угадайку слов!")
    print(display_hangman(tries))
    print(word_completion)
    while tries > 0:
        answer = input("Введите букву угадываемого слова или всё слово целиком").upper()
        while not answer.isalpha() and not answer in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
            print("Ты шо, дурачок? Нужно вводить буквы. Буквы кириллицы. Ничего другого не надо")
            answer = input().upper()
        while answer in guessed_letters:
            print("Ты уже называл эту букву, назови другую (или целое слово)")
            answer = input().upper()
        while answer in guessed_words:
            print("Ты уже называл это слово, назови другое (или одну букву)")
            answer = input().upper()
        if answer in word and len(answer) == 1:
            guessed_letters += answer
            guessed = True
            print("Ты угадал букву!")
            for i in range(len(word)):
                if word[i] == answer:
                    word_completion = word_completion[:i] + answer + word_completion[i + 1:]
            print(word_completion)
            print(display_hangman(tries))
            if word_completion.isalpha():
                guessed = True
                print("Ты угадал слово! Поздравляю!")
                print(word)
                break
        elif answer in word_list and len(answer) > 1:
            guessed = True
            print("Ты угадал слово! Поздравляю!")
            print(word)
            break
        elif not answer in word and len(answer) == 1:
            guessed_letters += answer
            guessed = False
            print("Не угадал!")
            print(word_completion)
            if not guessed:
                tries -= 1
            print(display_hangman(tries))
        elif not answer in word_list and len(answer) > 1:
            guessed_words += answer
            guessed = False
            print("Не угадал!")
            print(word_completion)
            if not guessed:
                tries -= 1
            print(display_hangman(tries))
        if tries == 0:
            print("Что ж, пошли вешаться...")
            break


play(get_word())


def restart():
    while True:
        if continue_game():
            play(get_word())
        else:
            print("До свидания!")
            break


restart()









