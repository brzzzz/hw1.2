
#Преобразование даты из американского формата в европейский

         #0123456789
amdate = '05.17.2016'
lst = (amdate.split('.'))
eurodate = ('%s.%s.%s' % (lst[1], lst[0], lst[2]))
print(eurodate)

# Преобразование имени

s = 'Mark Zuckerberg'
a, b = (s.split(' '))
print(b, a)

# Преобразование из формата snake_style в CamelizedStyle

snake_style = 'employee_first_name'
lst = (snake_style.split('_'))
result = lst[0].title() + lst[1].title() + lst[2].title()
print(result)


# Программа, которая по переданной строке определит возраст писателя и вернет его имя и возраст
# по формату

writers_data = 'Leo Tolstoy*1828-08-28*1910-11-20'
lst = writers_data.split('*')


def writers_age(writers_death, writers_birth):
    result = writers_death - writers_birth
    return result


result1 = writers_age(1910, 1828)

print(lst[0], result1)









#date = (amdate[3:5])
#month = (amdate[:2])
#year = (amdate[6:])



#print('%s %d %d %d') % (amdate, date, month, year))


#month, date, year = (amdate.split('.'))
#print(date, month, year)


#var = amdate.split('.')
#date = str(amdate[3:5])
#month = str(amdate[:2])
#year = str(amdate[6:])















