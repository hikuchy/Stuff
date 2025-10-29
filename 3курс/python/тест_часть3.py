from tkinter import *
class application(Frame):
    def __init__(self, fr):
        super(application, self).__init__(fr)
        self.grid()
        self.widget()    # Вопрос 1
        self.widget2()   # Вопрос 2
        self.widget3()   # Вопрос 3
        self.widget4()   # Вопрос 4

# Вопрос 1 с флажками
    def control(self):
        if self.otvet1.get() and self.otvet2.get() and self.otvet4.get() and not self.otvet3.get():
            p = "Ответ правильный"
        else:
            p = "Ответ неправильный"
        self.textbox2.delete(0.0, END)
        self.textbox2.insert(0.0, p)

    def widget(self):
        Label(self,
              text="Алгоритм может быть представлен:", 
              font=("Times New Roman", 16), fg="red"
              ).grid(row=0, column=0, sticky=W)

        Label(self,
              text="Выберите все верные ответы",
              font=("Times New Roman", 12),fg="green"
              ).grid(row=1, column=0, sticky=W)

        self.otvet1 = BooleanVar()
        Checkbutton(self,
                   text="В виде словесного описания",
                   font=("Times New Roman", 11),
                   variable=self.otvet1
                   ).grid(row=2, column=0, sticky=W)

        self.otvet2 = BooleanVar()
        Checkbutton(self,
                   text="Таблицы",
                   font=("Times New Roman", 11),
                   variable=self.otvet2
                   ).grid(row=3, column=0, sticky=W)

        self.otvet3 = BooleanVar()
        Checkbutton(self,
                   text="Графика",
                   font=("Times New Roman", 11),
                   variable=self.otvet3
                   ).grid(row=4, column=0, sticky=W)

        self.otvet4 = BooleanVar()
        Checkbutton(self,
                   text="Схемы",
                   font=("Times New Roman", 11),
                   variable=self.otvet4
                   ).grid(row=5, column=0, sticky=W)

        self.btn = Button(self,
                         text="Ответить",
                         command=self.control,
                         width=10,
                         height=2,
                         font=("Arial", 12))
        self.btn.grid(row=6, column=0, sticky=W)

        self.textbox2 = Text(self,
                            width=30,
                            height=2,
                            font=("Times New Roman", 12),
                            fg="red")
        self.textbox2.grid(row=7, column=0, sticky=W)

# Вопрос 2 с флажками
    def control2(self):  
        if self.otvet5.get() and self.otvet6.get() and self.otvet7.get() and self.otvet8.get():
            p = "Ответ правильный"
        else:
            p = "Ответ неправильный"
        self.textbox3.delete(0.0, END)
        self.textbox3.insert(0.0, p)

    def widget2(self):  
        Label(self,
              text="Что служит для графического представления объектов ОС Windows:",
              font=("Times New Roman", 14), fg="purple"
              ).grid(row=8, column=0, sticky=W)

        Label(self,
              text="Выберите все верные ответы",
              font=("Times New Roman", 12)
              ).grid(row=9, column=0, sticky=W)

        self.otvet5 = BooleanVar()
        Checkbutton(self,
                   text="Окна",
                   font=("Times New Roman", 11),
                   variable=self.otvet5
                   ).grid(row=10, column=0, sticky=W)

        self.otvet6 = BooleanVar()
        Checkbutton(self,
                   text="Кнопки",
                   font=("Times New Roman", 11),
                   variable=self.otvet6
                   ).grid(row=11, column=0, sticky=W)

        self.otvet7 = BooleanVar()
        Checkbutton(self,
                   text="Значки",
                   font=("Times New Roman", 11),
                   variable=self.otvet7
                   ).grid(row=12, column=0, sticky=W)

        self.otvet8 = BooleanVar()
        Checkbutton(self,
                   text="Ярлыки",
                   font=("Times New Roman", 11),
                   fg="purple",
                   variable=self.otvet8
                   ).grid(row=13, column=0, sticky=W)

        self.btn2 = Button(self,
                          text="Ответить",
                          command=self.control2,
                          width=10,
                          height=2,
                          font=("Arial", 12))
        self.btn2.grid(row=14, column=0, sticky=W)

        self.textbox3 = Text(self,
                           width=30,
                           height=2,
                           font=("Times New Roman", 14),
                           fg="red")
        self.textbox3.grid(row=15, column=0, sticky=W)

# Вопрос 3 с переключателями
    def control3(self):
        p = self.otvet9.get()
        if p == "Сделать код программы более лёгким для понимания":
            result = "Ответ правильный"
        else:
            result = "Ответ неправильный"
        self.textbox4.delete(0.0, END)
        self.textbox4.insert(0.0, result)

    def widget3(self):
        Label(self,
              text="Цель рефакторинга - это:",
              font=("Times New Roman", 14), fg="purple"
              ).grid(row=16, column=0, sticky=W)

        Label(self,
              text="Выберите правильный ответ",
              font=("Comic Sans MS", 12)
              ).grid(row=17, column=0, sticky=W)

        self.otvet9 = StringVar()
        self.otvet9.set(None)
        
        Radiobutton(self,
                   text="Сделать код программы более лёгким для выполнения", font=("Comic Sans ", 13),
                   variable=self.otvet9,
                   value="Сделать код программы более лёгким для выполнения"
                   ).grid(row=18, column=0, sticky=W)
        
        Radiobutton(self,
                   text="Сделать код программы более лёгким для понимания",font=("Arial", 13),
                   variable=self.otvet9,
                   value="Сделать код программы более лёгким для понимания"
                   ).grid(row=19, column=0, sticky=W)
        
        Radiobutton(self,
                   text="Ускорить выполнение программы",font=("Arial", 13),
                   variable=self.otvet9,
                   value="Ускорить выполнение программы"
                   ).grid(row=20, column=0, sticky=W)

        self.btn3 = Button(self,
                          text="Ответить",
                          command=self.control3,
                          width=10,
                          height=2,
                          font=("Arial", 12))
        self.btn3.grid(row=21, column=0, sticky=W)

        self.textbox4 = Text(self,
                            width=30,
                            height=2,
                            font=("Arial", 12),
                            fg="red")
        self.textbox4.grid(row=22, column=0, sticky=W)

# Вопрос 4 с переключателями
    def control4(self):
        p = self.otvet10.get()
        if p == "Упрощение структуры кода":
            result = "Ответ правильный"
        else:
            result = "Ответ неправильный"
        self.textbox5.delete(0.0, END)
        self.textbox5.insert(0.0, result)

    def widget4(self):
        Label(self,
              text="Что НЕ является целью рефакторинга:",
              font=("Times New Roman", 14), fg="green"
              ).grid(row=0, column=1, sticky=W)

        Label(self,
              text="Выберите правильный ответ",
              font=("Times New Roman", 12)
              ).grid(row=1, column=1, sticky=W)

        self.otvet10 = StringVar()
        self.otvet10.set(None)
        
        Radiobutton(self,
                   text="Улучшение читаемости кода",
                   font=("Comic Sans MS", 13),
                   variable=self.otvet10,
                   value="Улучшение читаемости кода"
                   ).grid(row=2, column=1, sticky=W)
        
        Radiobutton(self,
                   text="Исправление ошибок в программе",
                   font=("Comic Sans MS", 13),
                   variable=self.otvet10,
                   value="Исправление ошибок в программе"
                   ).grid(row=3, column=1, sticky=W)
        
        Radiobutton(self,
                   text="Упрощение структуры кода",
                   font=("Comic Sans MS", 13),
                   variable=self.otvet10,
                   value="Упрощение структуры кода"
                   ).grid(row=4, column=1, sticky=W)

        self.btn4 = Button(self,
                          text="Ответить",
                          command=self.control4,
                          width=10,
                          height=2,
                          font=("Arial", 12))
        self.btn4.grid(row=5, column=1, sticky=W)

        self.textbox5 = Text(self,
                            width=30,
                            height=2,
                            font=("Times New Roman", 12),
                            fg="red")
        self.textbox5.grid(row=6, column=1, sticky=W)

root=Tk()
root.title("Тест по алгоритмизации")
root.geometry("1920x1080") 
app=application(root)
root.mainloop()
