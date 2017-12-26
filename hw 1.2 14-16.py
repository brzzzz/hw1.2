import math


#Написать функцию, которая будет проверять четность некоторого числа.


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


def is_intersected(x1, y1, r1, x2, y2, r2):
    center_to_center_distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    radius_sum = r1 + r2
    if center_to_center_distance >= radius_sum:
        print('Не пересекаются')
        return True
    else:
        print('Пересекаются')
        return False


x1 = (int(input('Введите координаты центра первой окружности по горизонтали:')))
y1 = (int(input('Введите координаты центра первой окружности по вертикали:')))
x2 = (int(input('Введите координаты центра второй окружности по горизонтали:')))
y2 = (int(input('Введите координаты центра второй окружности по вертикали:')))
r1 = (int(input('Введите длину радиуса первой окружности:')))
r2 = (int(input('Введите длину радиуса второй окружности:')))
is_intersected(x1, y1, r1, x2, y2, r2)



