from math import sqrt

def is_fib(n):
    if sqrt(5 * (n ** 2) - 4) % 1 == 0 or sqrt(5 * (n ** 2) + 4) % 1 == 0: # Условие, которое характерно для чисел Фибоначчи
        return True
    else:
        return False

def ghost_age(opacity):
    age = 0
    current_opacity = 10000
    while current_opacity != opacity:
        age += 1
        if is_fib(age):
            current_opacity -= age
        else:
            current_opacity += 1
        if age > 5000:  # Привидения не бывают старше 5000 лет
            return None
    return age

# Примеры использования функции ghost_age для определения возраста по прозрачности
examples_transparency = [10000, 9999, 9997, 9994, 9995, 9990,6600,3400, 2300]
for transparency in examples_transparency:
    age = ghost_age(transparency)
    print(f"прозрачность = {transparency}, возраст: {age}")
