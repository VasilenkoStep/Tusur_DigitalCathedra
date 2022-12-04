print("Задача №1: Не уникальные элементы")

# Нужно получить массив, состоящий только из неуникальных элементов данного массива.\n
# Для этого необходимо удалить все уникальные элементы (которые присутствуют в данном массиве только один раз).\n
# Для решения этой задачи не меняйте оригинальный порядок элементов. \n
# Пример: [1, 2, 3, 1, 3], где 1 и 3 неуникальные элементы и результат будет [1, 3, 1, 3].\n
def CreateNotUniqArray (numb_array):
    num_set = set(numb_array)
    help_num_set = set()
    copy2_numb_array = numb_array.copy() # Используется для отбрасывания каждой цифры во множестве
    copy1_numb_array = numb_array.copy() # Используется для отбрасывания лишней цифры из изначального списка
    for num in num_set:
        # При помощи 2-ух множеств происходит проверка наличия более двух вхождений числа
        num_set = set(copy2_numb_array) # множество до удаления
        copy2_numb_array.remove(num)
        help_num_set = set(copy2_numb_array) # множество после удаления
        if num_set == help_num_set:
            continue
        else:
            copy1_numb_array.remove(num)
    print("Изначальный список:", numb_array, end=". Результат: ")
    return copy1_numb_array

numb_arr1 = [5, 5, 5, 5, 5]
numb_arr2 = [10, 9, 10, 10, 9, 8]
numb_arr3 = [1, 2, 3, 4, 5]
print(CreateNotUniqArray(numb_arr1))
print(CreateNotUniqArray(numb_arr2))
print(CreateNotUniqArray(numb_arr3))
