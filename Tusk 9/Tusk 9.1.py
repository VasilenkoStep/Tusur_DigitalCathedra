# 1. Список из числа.
# Дано: натуральное число N.
# Задание: написать функцию, которая возвращает список всех цифр этого числа в обратном порядке.
# Пример:  123, результат: [3, 2, 1]
def reverse_digits(n):
    # Преобразуем число в строку
    num_str = str(n)

    # Развернем строку и преобразуем каждый символ обратно в число
    reversed_digits = [int(digit) for digit in reversed(num_str)]

    return reversed_digits
# Пример использования
number = 123
result = reverse_digits(number)
print(result)