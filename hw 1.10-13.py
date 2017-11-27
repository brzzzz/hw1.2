import math

#---------------------------------------------------
# Написать функцию, которая будет переводить градусы в радианы. Используя эту функцию вывести
# на экран значения косинусов углов в 60, 45 и 40 градусов.


def degrees_to_radians(degrees):
    result = degrees * math.pi / 180
    return result


var = degrees_to_radians(60)
var1 = degrees_to_radians(45)
var2 = degrees_to_radians(40)

result1 = math.cos(var)
result2 = math.cos(var1)
result3 = math.cos(var2)

print('Результат фунции перевода градусов в радианы при 60 будет равен %f, при 45 будет равен %f и 40 равен %f,' %
      (var, var1, var2))
print('при этом значения консинсов углов для 60 градусов будут равны %.1f, для 45 равно %f и для 40 равно %f'
      % (result1, result2, result3))


#----------------------------------------------------
# Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа, введенного
# пользователем в консоли, без использования операторов цикла.
# Реализовать задачу без использования строк


def amount(number):
    numeral = number // 100
    numeral1 = number % 100 // 10
    numeral2 = number % 10
    result = numeral + numeral2 + numeral1
    return result


result1 = amount(123)

print('Результат суммы трёхзначного числа 123 будет равен %d' % result1)


#----------------------------------------------------
# Пользователь вводит длины катетов прямоугольного треугольника.
# Написать функцию, которая вычислит площадь треугольника и его периметр.
# Результат работы функции вывести на печать.

a = 5
b = 5


def triangle_data(a, b):
    triangle_square = 0.5 * a * b
    triangle_perimeter = a * 2 + b
    print('Площадь треугольника и его периметр равны %.1f сантиметров квадратных и %.f сантиметров'
          % (triangle_square, triangle_perimeter))
    return triangle_square, triangle_perimeter


triangle_data(a, b)



