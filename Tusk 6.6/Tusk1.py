print("Задача №1: Последний с четными")
num_list = [1, 3, 5]
count = 0
if num_list:
    for i in range(0,len(num_list), 2):
        count += num_list[i]
    count *= num_list[-1]
    print("Результат:", count)
else:
    print("Результат: 0")
