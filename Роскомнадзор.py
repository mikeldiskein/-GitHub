word = input() + ' запретил букву'
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
were = []
for i in range(len(alphabet)):
    if len(were) == 0:
        if alphabet[i] in word:
            were.append(alphabet[i])
    else:
        if alphabet[i] in word and not alphabet[i] in were:
            were.append(alphabet[i])
flag = False
for i in were:
    if not flag:
        word = word.replace('  ', ' ')
        print(word.strip() + ' ' + i)
        word = word.replace(i, '')
        flag = True
    elif flag:
        word = word.replace('  ', ' ')
        print(word.strip() + ' ' + i)
        word = word.replace(i, '')
