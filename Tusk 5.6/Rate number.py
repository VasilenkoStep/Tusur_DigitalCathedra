print("Задача №2: Оценка числа")
value = int(input("Введите число больше 0: "))
if value % 2 != 0:
    print('x = {num} - нечетное. "Плохо!"'.format(num=value))
elif 2 <= value <= 5 and value % 2 == 0:
    print('x ∈ [2, 5] и четное. "Неплохо!"'.format(num=value))
elif 6 <= value <= 20 and value % 2 == 0:
    print('x ∈ [6, 20] и четное.  "Так себе"'.format(num=value))
elif value > 20 and value % 2 == 0:
    print('x > 20 и четное.  "Отлично"'.format(num=value))
