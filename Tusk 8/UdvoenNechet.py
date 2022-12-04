import random
print("Задача №2: Перестановки.")
# нужно получить список "удвоенных" нечетных чисел от 0 до n.
n = random.randint(0, 25)
print("Число n: ", n)
numb_array = [x*2 for x in range(1, n+1, 2)]
print(numb_array)
