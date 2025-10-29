#metod find
text = input("Введите что-то: ")
word = input("Введите слово для исключения: ")
position = text.find(word)
if position != -1:
    text1 = text.replace(word, "")
    print(text1)
else:
    print("Заданное слово отсутствует в тексте")
