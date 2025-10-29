#metod index
text = input("Введите что-то: ")
word = input("Введите слово для исключения: ")
try:
    position = text.index(word)
    text1 = text.replace(word, "")
    print(text1)
except ValueError:
    print("СЛово", word, "не найдено в заданном тексте")
