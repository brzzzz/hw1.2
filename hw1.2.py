
#Преобразование даты из американского формата в европейский

         #0123456789
am_date = '05.17.2016'
lst = (am_date.split('.'))
eu_date = ('%s.%s.%s' % (lst[1], lst[0], lst[2]))
print(eu_date)


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
birth_date = lst[1]
death_date = lst[2]
year1 = birth_date.split('-')[0]
year2 = death_date.split('-')[0]
years_of_life = int(year2) - int(year1)
print(lst[0], years_of_life)













