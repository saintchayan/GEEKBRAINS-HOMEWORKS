# task3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
x1, x2, x3 = float(input('Введите первый агрумент: ')), float(input('Введите второй агрумент: ')), \
             float(input('Введите третий агрумент: '))
def func1(x1, x2, x3):
    if (x1 + x2) > (x2 + x3):
        print('Сумма наибольших двух аргументов: ', x1 + x2)
    elif (x2 + x3) > (x1 + x3):
        print('Сумма наибольших двух аргументов: ', x2 + x3)
    else:
        print('Сумма наибольших двух аргументов: ', x1 + x3)
    return x1, x2, x3
func1(x1, x2, x3)
