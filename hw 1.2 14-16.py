import math


# Написать функцию, которая будет проверять четность некоторого числа.


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


number = int(input('Введите Число:'))

is_even(number)

if is_even(number):
    print('{0} - Чётное'.format(number))
else:
    print('{0} - Нечётное'.format(number))




#---------------------------------------------------------------------------------
# Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.
# Каждая окружность задается координатами центра и радиусом.


x1 = 7
x2 = 5
y1 = 5
y2 = 7
r1 = 2
r2 = 2

center_to_center_distance = (x1 - x2) ** 2 + (y1 - y2) ** 2

radius_sum = r1 + r2


def is_intersect(center_to_center_distance, radius_sum):
    if center_to_center_distance <= radius_sum:
        print('Не пересекаются')
        return True
    else:
        print('Пересекаются')
        return False


is_intersect(center_to_center_distance, radius_sum)










