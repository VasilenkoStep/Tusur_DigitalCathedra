print("Задача №4: Секретное сообщение")
text = input("Введите зашифрованный текст: ")
secret_word = ' '
for i in text:
    if i.isupper():
        secret_word += i
    else:
        continue
print("Полученное сообщение:", secret_word)
