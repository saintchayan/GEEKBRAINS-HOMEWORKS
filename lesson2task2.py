# task2
print('Заполните список необходимыми элементами:')
a = [int(x) for x in input().split()]
for i in range(0, len(a)-1, 2):
    a[i], a[i + 1] = a[i + 1], a[i]
print(" ".join(str(i) for i in a))


