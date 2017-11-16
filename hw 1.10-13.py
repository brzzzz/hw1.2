import math

#---------------------------------------------------
# Написать функцию, которая будет переводить градусы в радианы. Используя эту функцию вывести
# на экран значения косинусов углов в 60, 45 и 40 градусов.


def degrees_to_radians(degrees):
    result = degrees * math.pi / 180
    return result


result1 = degrees_to_radians(60)
result2 = degrees_to_radians(45)
result3 = degrees_to_radians(40)

print('Резудьтат фунции перевода градусов в радианы при 60 будет равен %f, при 45 будет равен %f и 40 равен %f' %
      (result1, result2, result3))


#----------------------------------------------------
# Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа, введенного
# пользователем в консоли, без использования операторов цикла.
# Реализовать задачу без использования строк
