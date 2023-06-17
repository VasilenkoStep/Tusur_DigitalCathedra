print("Задача №2: Max-min")
num_list = [10.2, -2.2, 0, 1.1, 0.5]
count = 0
if num_list:
    Max = max(num_list)
    Min = min(num_list)
    print("результат: {0:,.3f}".format(Max-Min))
else:
    print("Результат: 0")
