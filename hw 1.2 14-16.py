# Написать функцию, которая будет проверять четность некоторого числа.


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


number = int(input('Число?'))

is_even(number)

if is_even(number):
    print('{0} - Чёт'.format(number))
else:
    print('{0} - Нечет'.format(number))




#---------------------------------------------------------------------------------
# Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.
# Каждая окружность задается координатами центра и радиусом.


