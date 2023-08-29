'''
2.	Имеется список, состоящий из чисел.
Напишите функцию которая принимает число и возвращает список состоящий из элементов первого списка кратных входному параметру.

'''

test_list = [1, 2, 3, 4, 5, 6, 8, 9, 12, 15, 18]


def multiples(test_list, param):
    res = []
    for num in test_list:
        if num % param == 0:
            res.append(num)
        else:
            pass
    return res


print(multiples(test_list, 3))
print(multiples(test_list, 2))
