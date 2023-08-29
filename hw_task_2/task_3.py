"""
3.	Напишите функцию, которая принимает
любое количество не именованных аргументов и
возвращает кортеж состоящий из аргументов у которых тип данных str
"""

def str_filter(*args):
    res = []
    for elem in args:
        if type(elem) == str:
            res.append(elem)

    return tuple(res)

print(str_filter(1,'1',2,'two',[1,2,3],False,'three','four'))
