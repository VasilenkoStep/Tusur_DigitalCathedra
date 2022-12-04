print("Задача №3: Ленивый спекулянт")
rates = {'Sberbank': 57.8, 'VTB24': 56, 'SovkomBank': 56.1, 'HalvaBank': 65.9, 'Dinkoff': 56}
if len(rates) == 0:
    print('Ошибка: Нет данных')
else:
    min_rate = min(rates.values())

# сложность O(n). Проход по каждому элементу и проверка его ставки на минимальное значение
for key, value in rates.items():
    if value == min_rate:
        print("Банк с минимальной ставкой: {bank} -> {value}".format(bank=key, value=value))

# Или уже новое решение через генератор списка
bank_list = [key for key, value in rates.items() if value == min_rate]
print("Банки с минимальной ставкой:", bank_list)
