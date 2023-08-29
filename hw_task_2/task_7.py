"""
7.	Напишите декоратор который запускает декорируемую функцию повторно,
в случае если произошло исключение при первом запуске.
Напишите 2 тестовые декорируемые функции с произвольными данными.

"""

def repeat(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except:
            print('First attempt ends with exeption')
            res = func(*args, **kwargs)
        return res

    return wrapper


i = 0
@repeat
def Exeption_raiser():
    global i
    i = i + 1
    if i == 1:
        raise Exception

@repeat
def counter(a=[0]):
    a[0] += 1
    if a[0] == 1:
        raise Exception


Exeption_raiser()
counter()