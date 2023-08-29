'''
Напишите функцию которая возвращает длину принимаемой строки, по умолчанию строка пустая (s=’’).
Пропишите все аннотации
'''


s = ''


def string_lengh(s: str) -> int:
    return len(s)


print(string_lengh(s))
print(string_lengh('123'))
print(string_lengh('Мама мыла раму'))
print(string_lengh(123))