# task1
"""
Создать класс TrafficLight (светофор).

определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
— на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение
и завершать скрипт.

"""

from time import sleep

class TrafficLight:
    # атрибуты класса
    __color = ('Красный', 'Желтый', 'Зеленый')

    # метод
    def running(self):
        i = 0
        while i < 3:
            print(f'Переключение светофора {TrafficLight.__color[i]}')

            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(7)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()