from random import randint
print("Задача №1: Среднее")
num1, num2, num3 = randint(0, 100), randint(0, 100), randint(0, 100)
aver_value = (num1+num2+num3)/3
print("Используемые числа: {}, {}, {}".format(num1, num2, num3))
print("Среднее значение: {0:.2f}".format(aver_value))
