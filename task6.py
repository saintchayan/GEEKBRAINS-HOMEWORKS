# task6
print('Укажите количество километров в первый день:')
a = float(input())
print('Укажите желаемую дистанцию, которую хочет спортсмен достичь:')
b = float(input())
counter = 1
while b > a:
    print('{}-й день : {}'.format(counter, a))
    a = a + 0.1 * a
    counter = counter + 1
print('{}-й день : {}'.format(counter, a))
