print("Задача №2: Римские цифры")
num = int(input("Введите число от 1 до 3999: "))
def num_to_roman(number):
    units_list = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens_list = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds_list = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousand_list = ["", "M", "MM", "MMM", "MMMM"]

    t = thousand_list[number // 1000]
    h = hundreds_list[number // 100 % 10]
    te = tens_list[number // 10 % 10]
    o = units_list[number % 10]

    return t + h + te + o
print(num_to_roman(num))