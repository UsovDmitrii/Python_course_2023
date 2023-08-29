""""
Напишите функцию которая
a)	на вход получает строковую переменную.
i)	в строке содержится несколько слов
b)	Возвращает строку состоящую из аббревиатур слов переменной.
c)	Если на вход поступил другой тип данных, должно срабатывать исключение
d)	Результат работы функции распечатайте в консоль
"""


def abbreviation(string):

    try:
        abbr = ''
        word_list = string.split(' ')
        if len(word_list) > 1:
            for word in word_list:
                lit = word[0].upper()
                abbr = abbr + lit
            print(abbr)
        else:
            raise Exception('Входная строка должна содержать слова, разделенные пробелами')
    except AttributeError:
        raise Exception('Функция принимает на вход стороку')


string_1 = 'Служба погодного мониторинга'
abbreviation(string_1)
#abbreviation(123)
abbreviation('Служба')
