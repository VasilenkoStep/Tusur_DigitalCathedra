# 4. Дешифратор.
# Дано: шифровальная решетка (4 на 4) и зашифрованный пароль (4 на 4) представлены, как массив строк.
#
# Задание. Помогите Софи написать дешифратор для паролей, которые Никола зашифровал с помощью шифровальной решетки.
# Шифрорешетка - это квадрат 4 на 4 с четырьмя вырезанными окошками. Поместите решетку на листе бумаги такого
# же размера с буквами, выписываете первые 4 символа, которые видно в окошках (см. рисунок).
# Затем поверните решетку на 90 градусов по часовой стрелке. Выпишите следующие символы и повторите поворот.
# В итоге процедура повторяется 4 раза. Таким образом сложно узнать пароль без специальной решетки.
#
# Напишите программу, которая поможет проводить данную процедуру.

def decrypt_password(grid, password):
    decrypted_password = ""
    for _ in range(4):
        decrypted_password += "".join(password[ii][iii]
                                      for ii, row in enumerate(grid) # Выделение позиции строки {ii} и самой строки в решетке для поиска X
                                      for iii, cell in enumerate(row) if cell == 'X') # Выделение позиции ячейки {iii} и самой ячейки с X
        grid = rotate_grid(grid)
    return decrypted_password


def rotate_grid(grid):
    return ["".join(grid[i][j] for i in range(3, -1, -1)) for j in range(4)]


# Примеры
grid_1 = [
    'X...',
    '..X.',
    'X..X',
    '....'
]
password_1 = [
    'itdf',
    'gdce',
    'aton',
    'qrdi'
]
print(decrypt_password(grid_1, password_1))  # icantforgetiddqd

grid_2 = [
    '....',
    'X..X',
    '.X..',
    '...X'
]
password_2 = [
    'xhwc',
    'rsqx',
    'xqzz',
    'fyzr'
]
print(decrypt_password(grid_2, password_2))  # rxqrwsfzxqxzhczy