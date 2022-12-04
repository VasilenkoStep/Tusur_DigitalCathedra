print("Задача №2: Перестановки.")
x, y, z, n = map(int, input("Введите 4 числа, для перестановки: ").split())
# нужно получить список всех возможных перестановок чисел x, y, z, где x + y + z != n.
num_list = [x, y, z]
swap_array = [[i, j, k]
              for i in range(x+1)
              for j in range(y+1)
              for k in range(z+1)
              if i+j+k != n]
print(swap_array)
