#Элементарная задача
print()
print('Задача №1')
print('Сколько месяцев в году?')
my_int = int(input('Ваш ответ: '))
my_bool = bool(my_int)

if (my_int != 12):
    print(not my_bool, 'ответ', my_int, 'не верный, не грусти)!')
else:
    print(my_bool, 'ответ', my_int, 'верный,Молодец!')

# Программа которая определяет
# соответствует ли введенное число следующим критериям:
# 1. Число трехзначное
# 2. Число не парное
# 3. Число делится без остатка на 37
# Примеры правильных значений - 185, 555, 925
print()
print('Задача №2, это уже по сложнее))')
my_int = int(input('Введите трёхзначное не парное число которое делится на 37: '))
my_bool = bool(my_int)

if (1 <= (my_int / 100) < 10) and (my_int % 2 != 0) and (my_int % 37 == 0):
    print(my_bool, 'число', my_int, 'соответствует условиям')
else:
    print(not my_bool, 'число', my_int, 'не соответствует условиям!')
