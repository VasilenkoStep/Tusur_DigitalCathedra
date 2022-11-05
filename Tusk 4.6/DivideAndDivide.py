from random import randint
print("Задача №2: Деление и еще раз деление")
num1, num2, = randint(0, 100), randint(0, 100)
int_division = num1//num2 if num1 > num2 else num2//num1
remainder_division = num1 % num2 if num1 > num2 else num2 % num1
print("Используемые числа: {}, {}".format(num1, num2))
print("Результат целочисленного деления: {}".format(int_division))
print("Остаток от деления: {}".format(remainder_division))
