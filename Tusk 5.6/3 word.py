print("Задача №5: Три слова")
text = input("Введите текст: ")
count = 0
for w in text.split(" "):
    # Отделение каждого слова и их подсчет
    if w.isalpha():
        count += 1
        if count == 3:
            print("True")
    else:
        count = 0
if count != 3:
    print("False")
