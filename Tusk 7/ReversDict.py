print("Задача №4: Вверх дном")
rates = {'Sberbank': 57.8, 'VTB24': 56, 'SovkomBank': 56.1, 'HalvaBank': 65.9, 'Dinkoff': 56}
revers_rates = {value: key for key, value in rates.items()}
print("Изначальный словарь:", rates)
print("Словарь вверх дном:", revers_rates)
