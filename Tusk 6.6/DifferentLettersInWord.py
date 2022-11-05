print("Задача №5: Полосатые слова")
text1 = "2 a quan2tity of striped words."
vowels = ["A", "E", "I", "O", "U", "Y"]
consonants = ["B", "C", "D", "F", "G", "H", "J",
              "K", "L", "M", "N", "P", "Q",
              "R", "S", "T", "V", "W", "X", "Z"]
count = 0
word_accept = True    # необходимо для проверки слова на "полосатость"
text2 ="My name is ..."
text3 ="Dog,cat,mouse,bird.Human."
# Функция для удаления лишних знаков и цифр, и последующему приведение к списку
def clean_text(text):
    print("text =", text)
    string = " "
    # Чтобы не добавлять нижний регистр в массивы букв
    # просто перевожу изначальный текст к заглавным буква, данным по заданию
    text = text.upper()
    for i in text:
        if i.isalpha():
            string += i
            continue
        elif i.isdigit():
            string = string+i.replace(i, "")
        else:
            string = string + i.replace(i, " ")
    string_list = string.split() # легче обрабатывать слова в списке
    return string_list

for word in clean_text(text3):
    if len(word) == 1:
        continue
    for letter in range(len(word)-1):
        # Проверка на чередование букв
        if ((word[letter] in vowels and word[letter+1] in consonants) or
            (word[letter] in consonants and word[letter+1] in vowels)):
            word_accept = True
        else:
            word_accept = False
            break
    if word_accept:
        count += 1
print("Результат:", count)
