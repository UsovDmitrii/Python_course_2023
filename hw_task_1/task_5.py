"""
Напишите функцию которая отвечает “ДА” или “НЕТ” на вопрос в комментарии
"""


def find_string(str_1, str_2):

    index = str_2.find(str_1)
    if index == -1:
        print('НЕТ')
    else:
        print('ДА')


str_1 = 'test'
str_2 = 'test1'
find_string(str_1, str_2)


str_3 = 'est1t'
find_string(str_1, str_3)

str_4 = 'tes1est2test'
find_string(str_1, str_4)
