x = input("введи число: ")

try:
    int(x)
except ValueError:
    print("Неправильный ввод значения")
else:
    print("Правильный ввод значения")











