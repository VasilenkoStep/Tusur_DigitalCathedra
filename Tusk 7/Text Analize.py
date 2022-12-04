import string
print("Задача №1: Анализ текста. Популярность.")
text = "hello, word ;of, word"
print("Изначальный текст:", text)
text.split(" ")
def letter_counter(text: str):
    chars_popularity = {}
    letter_count = 1

    for letter in text:
        if letter in chars_popularity:
            chars_popularity[letter] += 1
            continue
        chars_popularity[letter] = letter_count

    return chars_popularity


def words_counter(text: str):
    words_popularity = {}
    clean_text_list = text.split()
    words_count = 1

    for word in clean_text_list:
        if word in words_popularity:
            words_popularity[word] += 1
            continue
        words_popularity[word] = words_count

    return words_popularity


# str.translate() функция для удаления всех знаков препинания из строки.
# Сопоставляет каждый символ строки с таблицей перевода,
# которую можно легко создать с помощью str.maketrans() функции.
clean_text_str = text.translate(str.maketrans('', '', string.punctuation))
print("Подсчет вхождений букв: ", letter_counter(clean_text_str))
print("Подсчет вхождений слов: ", words_counter(clean_text_str))
# words_popularity = {'hello': 1, 'word': 2, 'of': 1}
