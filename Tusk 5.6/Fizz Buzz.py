print("Задача №1: Fizz Buzz")
value = int(input("Введите любое целое число: "))
if value % 3 == 0 and value % 5 == 0:
    print('x = {num}, результат: "Fizz Buzz"'.format(num=value))
elif value % 3 == 0 and value % 5 != 0:
    print('x = {num}, результат: "Fizz"'.format(num=value))
elif value % 3 != 0 and value % 5 == 0:
    print('x = {num}, результат: "Buzz"'.format(num=value))
else:
    print('x = {num}, результат: "{num}"'.format(num=value))
