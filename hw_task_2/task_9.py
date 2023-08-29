"""
9.	* Напишите декоратор который измеряет время выполнения декорируемой функции.

Напишите 2 тестовые декорируемые функции с произвольными данными.

"""


def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'Runtime :{end - start} seconds')
        return res

    return wrapper


@timer
def long_func(n):
    import time
    print(f'Estimated time is {n / 1000} seconds')
    time.sleep(n / 1000)
    print('All done')

@timer
def knot_num(n):
    return n ** (n ** n)


long_func(100)
knot_num(8)
