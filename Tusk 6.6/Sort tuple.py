print("Задача №3: Умная сортировка")
num_tuple = (10.2, -20, 0, -110, -0.5)
def abs_num_f(x):
    return abs(x)
num_list = [x for x in num_tuple]
num_list.sort(key=abs_num_f)
print(num_list)
