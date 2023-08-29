"""
5.	Лесенка.
Лесенкой - условный набор кубиков, в котором каждый последующий слой содержит меньше кубиков, чем предыдущий.
Напишите функцию, вычисляющую число лесенок, которое можно построить из n кубиков.
-	Длина каждой ступени может отличаться.
-	n - натуральное число в диапазоне от 1 до 100.

"""


def ladder(n, i=1):

    ll = n
    ul = 0
    while 0 <= ul <= ll :
        if ul ==0 :
            pass
        elif ll == ul:
            i = i + ladder(ul,i=0)
        else:
            i = i + ladder(ul)
        ll = ll - 1
        ul = ul + 1

    return i

print('1: ', ladder(1))
print('2: ', ladder(2))
print('3: ', ladder(3))
print('4: ', ladder(4))
print('5: ', ladder(5))
print('6: ', ladder(6))
print('7: ', ladder(7))
print('8: ', ladder(8))

print('100: ', ladder(100))
