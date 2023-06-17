import sys
print("Задача №4: Число наоборот")
value = int(input("Введите любое целое число: "))
new_value = 0
if sys.getsizeof(value) >= 32:
    print("Число вышло за границы типа ->", new_value)
else:
    list_of_number = list(str(value))
    if value > 0:
        for i in range(len(list_of_number)):
            new_value += int(list_of_number[i]) * pow(10, i)
    else:
        for i in range(len(list_of_number)-1):
            new_value += int(list_of_number[i+1])*pow(10, i)
        new_value = -new_value
    print("Число наоборот ->", new_value)

