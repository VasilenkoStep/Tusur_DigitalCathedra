print("Задача №4: Медиана")
num_list1 = [3, 6, 20, 99, 10, 15]
num_list2 = [3, 1, 2, 5, 3]
med_value = 0
def find_median(list_):
    # Нахождение медианы для четной длины списка
    list_.sort()
    if len(list_) % 2 == 0:
        med_value = (list_[len(list_)//2]+list_[len(list_)//2-1])/2
    # Нахождение медианы для нечетной длины списка
    else:
        med_value = list_[len(list_)//2]
    print("elements = {list}, результат: {num:,.3f}".format(list=list_, num=med_value))

find_median(num_list2)
find_median(num_list1)
