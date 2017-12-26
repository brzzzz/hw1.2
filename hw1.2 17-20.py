import math


# Написать функцию решения квадратного уравнения.
#         def solve_quadratic_equation(a, b, c): # returns 2 values: either 2 roots or 2 Nones
#             pass


def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(x1)
        print(x2)
    elif discriminant == 0:
        x = -b / (2 * a)
        print(x)
    else:
        print('Корней нет')


a = (int(input('Введите кофициэнт а:')))
b = (int(input('Введите кофициэнт b:')))
c = (int(input('Введите кофициэнт c:')))
solve_quadratic_equation(a, b, c)


# Каждому символу в таблице символов Unicode соответствует число.
# Написать функцию, которая рассчитывает сумму чисел, которые соответствуют символам,
# стоящим между двумя заданными включительно. Например, в функцию передаются символы ‘x’ и ‘z’.
# Значит надо вычислить сумму кодов символов ‘x’,’y’,’z’.
#         def sum_symbol_codes(first, last): # returns int
#             pass


