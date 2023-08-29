"""
Функция на вход получает 2 переменные.
a)	Кол-во лет (int)
b)	Кол-во месяцев (int)
Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.
"""


def days_conv(year: int, month: int) -> int:

    month_1 = year * 12
    days = (month_1 + month) * 29
    return days


year = 1
month = 0
print(days_conv(year,month))
print(days_conv(0, 0))
print(days_conv(1, 0))
print(days_conv(0.5, 8))
