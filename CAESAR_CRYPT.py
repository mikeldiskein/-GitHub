import string as s  # импортируем модуль string

good_answers = ('yes', 'да')
bad_answers = ('no', 'нет')
english_lower = s.ascii_lowercase
english_upper = s.ascii_uppercase
russian_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
russian_upper = russian_lower.upper()


def continue_game():  # предложение сыграть ещё раз
    reply = input('Do you want to try again?')
    while reply not in good_answers and reply not in bad_answers:
        reply = input("Write please 'yes'('да') or 'no'('нет')")
    if reply in good_answers:
        return True
    elif reply in bad_answers:
        return False


def crypt(p, k, d):  # сердце программы: алгоритм шифровки
    result = ''
    if d in ('encrypt', 'шифровка'):
        for i in p:
            if not i.isalpha:
                result += i
            elif i in s.punctuation:
                result += i
            elif i in english_upper:
                ind = english_upper.find(i)
                result += english_upper[(ind + k) % 26]
            elif i in english_lower:
                ind = english_lower.find(i)
                result += english_lower[(ind + k) % 26]
            elif i in russian_upper:
                ind = russian_upper.find(i)
                result += russian_upper[(ind + k) % 32]
            elif i in russian_lower:
                ind = russian_lower.find(i)
                result += russian_lower[(ind + k) % 32]
            elif i.isdigit:
                result += i
    elif d in ('decrypt', 'дешифровка'):
        for i in p:
            if not i.isalpha:
                result += i
            elif i in s.punctuation:
                result += i
            elif i in english_upper:
                ind = english_upper.find(i)
                result += english_upper[(ind - k) % 26]
            elif i in english_lower:
                ind = english_lower.find(i)
                result += english_lower[(ind - k) % 26]
            elif i in russian_upper:
                ind = russian_upper.find(i)
                result += russian_upper[(ind - k) % 32]
            elif i in russian_lower:
                ind = russian_lower.find(i)
                result += russian_lower[(ind - k) % 32]
            elif i.isdigit:
                result += i
    return result


def game():  # сама игра, собственно
    phrase = input('Write any word or phrase which you want to encrypt or decrypt')  # пользователь вводит фразу
    k = input('Write key: it must be an integer number') # пользователь вводит ключ
    while not k.isdigit():
        k = input('It must be an integer number')
    k = int(k)
    direction = input("Write what I should do: 'encrypt' ('шифровка') or 'decrypt' ('дешифровка')")
    while direction not in ('encrypt', 'decrypt', 'шифровка', 'дешифровка'):
        direction = input("'encrypt' ('шифровка') or 'decrypt' ('дешифровка')")
    print(crypt(p=phrase, k=k, d=direction))
    if continue_game():
        game()
    else:
        print('See you again!')


def begin():
    print('Приветствую Вас! Меня зовут Фейнман, и я предлагаю вам '  # приветствие и предложение сыграть
          'зашифровать или дешифровать какое-нибудь слово или'
          'предложение. Вы можете использовать как английский, так '
          'и русский язык')
    answer = input("Do you want to try? Write 'yes'('да') or 'no'('нет')").lower()
    while answer not in good_answers and answer not in bad_answers:
        answer = input("Write 'yes'('да') or 'no'('нет')")
    if answer in good_answers:
        game()
    else:
        print('Well, see you later!')


begin()




