# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"


dict = {'one': 'один',
        'two': 'два',
        'free': 'три',
        'four': 'чОтыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
        }


# def num_translate():
#     key = input('Введите слово для перевода: ')
#     if key:
#         print(f'Перевод слова: {dict.setdefault(key)}')
#     else:
#         print('Некорректные данные')

# def num_translate(word):
#     return dict.get(word)
#
# print(num_translate(input('Enter any number: ')))


def num_translate(word):
    if word.istitle():
        return str(dict.get(word.lower())).title()
    return dict.get(word)

print(num_translate(input('Enter any number: ')))

