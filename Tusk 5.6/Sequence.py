print("Задача №3: Последовательность")
value = int(input("Введите число ∈ [1-9]: "))
str_num = ' '
for i in range(value):
    str_num += str(i+1)
print(str_num)