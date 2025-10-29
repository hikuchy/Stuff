#metod in
text = input("Введите что-то: ")
word = input("Введите слово для исключения: ")
if word in text:
    text1 = text.replace(word, "")
    print(text1)
else:
    print("Такого слова нет в тексте")
