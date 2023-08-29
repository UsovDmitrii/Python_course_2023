"""
6.	Напишите декоратор который выводит исключение в случае если декорируемая функция возвращает тип данных отличный от int
Напишите 2 тестовые декорируемые функции с произвольными данными.
"""


def int_trigger(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if type(res) != int:
            raise Exception('Return type not int')
        else:
            return res

    return wrapper


@int_trigger
def return_int():
    return 1


@int_trigger
def not_return_int():
    return 'one'

print(return_int())
print(not_return_int())