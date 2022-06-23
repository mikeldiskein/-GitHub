import string as s

good_answers = ('yes', 'да')
bad_answers = ('no', 'нет')
english_lower = s.ascii_lowercase
english_upper = s.ascii_uppercase
russian_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
russian_upper = russian_lower.upper()


def continue_game():
    reply = input('Do you want to try again?')
    while True:
        if reply in good_answers:
            return True
        elif reply in bad_answers:
            return False
        else:
            print("Write please 'yes'('да') or 'no'('нет')")
            continue


def hack(phrase, language):
    results = []
    if language == 'en':
        for k in range(1, 27):
            result = ''
            for i in phrase:
                if i in s.punctuation:
                    result += i
                elif i == ' ':
                    result += i
                elif i in english_lower:
                    ind = english_lower.find(i)
                    result += english_lower[(ind - k)]
                elif i in english_upper:
                    ind = english_upper.find(i)
                    result += english_upper[(ind - k)]
                elif i.isdigit():
                    result += i
            results.append(result)
    else:
        for k in range(1, 33):
            result = ''
            for i in phrase:
                if i in s.punctuation:
                    result += i
                elif i == ' ':
                    result += i
                elif i in russian_lower:
                    ind = russian_lower.find(i)
                    result += russian_lower[(ind - k)]
                elif i in russian_upper:
                    ind = russian_upper.find(i)
                    result += russian_upper[(ind - k)]
                elif i.isdigit():
                    result += i
            results.append(result)
    print(f'{k} вариантов:')
    print(*results, sep='\n')


def game():
    language = input('In what language do you want to hack a phrase? en or ru?').lower()
    while language not in ('en', 'ru'):
        language = input('Write please en or ru')
    phrase = input('Write any word or phrase which you want to hack')
    hack(phrase, language)
    if continue_game():
        game()
    else:
        print('See you again!')


def begin():
    print('Hello you! It is Feinman again and I suggest you to hack some word or phrase '
          'from Caesar Crypt to your language. You can hack into english and into russian '
          'too')
    print("Do you want to try? Write 'yes'('да') or 'no'('нет')")
    answer = input()
    while True:
        if answer in good_answers:
            game()
            break
        elif answer in bad_answers:
            print('Well, see you later!')
            break
        else:
            answer = input("Write 'yes'('да') or 'no'('нет')")
            continue


begin()
        