import math


#Написать функцию, которая будет проверять четность некоторого числа.


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


number = int(input('Введите Число:'))

if is_even(number):
    print('{0} - Чётное'.format(number))
else:
    print('{0} - Нечётное'.format(number))
is_even(number)

# ---------------------------------------------------------------------------------
# Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.
# Каждая окружность задается координатами центра и радиусом.


def is_intersected(x1, y1, r1, x2, y2, r2):
    center_to_center_distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    radius_sum = r1 + r2
    radius1 = abs(r1 - r2)
    if radius_sum <= center_to_center_distance >= radius1:
        print('Пересекаются')
        return True
    else:
        print('Не пересекаются')
        return False


x1 = (int(input('Введите координаты центра первой окружности по горизонтали:')))
y1 = (int(input('Введите координаты центра первой окружности по вертикали:')))
x2 = (int(input('Введите координаты центра второй окружности по горизонтали:')))
y2 = (int(input('Введите координаты центра второй окружности по вертикали:')))
r1 = (int(input('Введите длину радиуса первой окружности:')))
r2 = (int(input('Введите длину радиуса второй окружности:')))
is_intersected(x1, y1, r1, x2, y2, r2)


# Два поезда движутся на скорости V1 и V2 навстречу друг другу.
# Между ними 10 км. пути. Через 4 км пути первый поезд может свернуть на запасной путь.
# При заданных скоростях узнать столкнутся ли поезда.
# def have_trains_crashed(v1, v2): # returns boolean value
#             pass

def have_trains_crashed(v1, v2):
    t1 = 4 / v1
    t2 = 6 / v2
    if t1 >= t2:
        print('Столкнуться')
        return True
    else:
        print('Первый поезд успеет на запасной путь')
        return False


v1 = (float(input('Введите скорость первого поезда:')))
v2 = (float(input('введите скорость второго поезда')))
have_trains_crashed(v1, v2)
