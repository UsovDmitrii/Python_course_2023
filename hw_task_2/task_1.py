"""
1.	Имеется строка состоящая из слов. Напишите функцию которая возвращает строку убрав из нее стоп слова.
Стоп слова находятся в списке:
"""

stop_words = ['Python', 'php', 'go', 'C']
test_list = ['programm', 'Python', 'lang', 'php', 'go', 'C', 'fast', 'framework']


def word_filter(list, stop):
    for word in list:
        if word in stop:
            list.pop(list.index(word))
        else:
            pass
    return list


print(word_filter(test_list,stop_words))
print(test_list)
