# 2.Палиндром.
# Дано: слово, состоящее только из строчных латинских букв.
# Задание: написать функцию, которая возвращает True, если слово палиндромом, иначе False.
# Примеры:
# 'lol', результат: True
# 'hi', результат: False

def is_palindrome(word):
    return word == word[::-1]

# Тестовые случаи
print(is_palindrome('lol'))  # Ожидаемый результат: True
print(is_palindrome('hi'))   # Ожидаемый результат: False