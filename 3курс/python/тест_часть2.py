#test
from tkinter import *
class application(Frame):
    def __init__(self,fr):
        super(application,self).__init__(fr)
        self.grid()
        self.widget()
        self.widget2()
        self.widget3()
        self.widget4()
    def control(self):
        if self.otvet1.get() and self.otvet2.get() and self.otvet4.get() and not self.otvet3.get():
            p="Ответ правильный"
        else:
            p="Ответ неправильный"
        self.textbox2.delete(0.0,END)
        self.textbox2.insert(0.0,p)
#Вопрос№1 с флажками
    def widget(self):
        Label(self,
              text="Алгоритм может быть представлен:",font=("Times New Roman",16),fg="red",
              ).grid(row=0, column=0, sticky=E)

        self.lbl=Label(self,text="Выберите все верные ответы"
                       ,font=("Times New Roman",12))
        self.lbl.grid(row=2,column=0, sticky=W)

        self.otvet1=BooleanVar()
        Checkbutton(self,
                    text="В виде словесного описания",font=("Times New Roman",11),
                    variable=self.otvet1
                    ).grid(row=3,column=0, sticky=W)

        self.otvet2=BooleanVar()
        Checkbutton(self,
                    text="Таблицы",font=("Times New Roman",11),
                    variable=self.otvet2
                    ).grid(row=4,column=0,sticky=W)
               
        self.otvet3=BooleanVar()
        Checkbutton(self,
                    text="Графика",font=("Times New Roman",11),
                    variable=self.otvet3
                    ).grid(row=5,column=0,sticky=W)
                    
        self.otvet4=BooleanVar()
        Checkbutton(self,
                    text="Схемы",font=("Times New Roman",11),
                    variable=self.otvet4
                    ).grid(row=6,column=0,sticky=W)

        self.btn=Button(self)
        self.btn["text"]="Ответить"
        self.btn["command"]=self.control
        self.btn["width"]=10
        self.btn["height"]=2
        self.btn["font"]=("Arial",12)
        self.btn.grid(row=7,column=0, sticky=W)

        self.textbox2=Text(self,width=30,height=2,font=("Times New Roman",12),fg="blue")
        self.textbox2.grid(row=10,column=0, sticky=W)

#Вопрос№2 с флажками

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
              ).grid(row=13, column=0, sticky=W)

        self.lbl2 = Label(self, text="Выберите все верные ответы", font=("Times New Roman", 12))
        self.lbl2.grid(row=14, column=0, sticky=W)

        self.otvet5=BooleanVar()
        Checkbutton(self,
                    text="Окна",font=("Times New Roman",11),
                    variable=self.otvet5
                    ).grid(row=15,column=0,sticky=W)

        self.otvet6=BooleanVar()
        Checkbutton(self,
                    text="Кнопки",font=("Times New Roman",11),
                    variable=self.otvet6
                    ).grid(row=16,column=0,sticky=W)
               
        self.otvet7=BooleanVar()
        Checkbutton(self,
                    text="Значки",font=("Times New Roman",11),
                    variable=self.otvet7
                    ).grid(row=17,column=0,sticky=W)
                    
        self.otvet8=BooleanVar()
        Checkbutton(self,
                    text="Ярлыки",font=("Times New Roman",11),fg="purple",
                    variable=self.otvet8
                    ).grid(row=18,column=0,sticky=W)

        self.btn2 = Button(self)  
        self.btn2["text"] = "Ответить"
        self.btn2["command"] = self.control2  
        self.btn2["width"]=10
        self.btn2["height"]=2
        self.btn2["font"]=("Arial",12)
        self.btn2.grid(row=19, column=0, sticky=W)

        self.textbox3 = Text(self, width=30, height=2, font=("Times New Roman", 14), fg="blue")  
        self.textbox3.grid(row=20, column=0, sticky=W)

#Вопрос№3 с переключателем
    def control3(self):
        p = self.otvet9.get()
        if p == "Сделать код программы более лёгким для понимания":
            result = "Ответ правильный"
        else:
                result = "Ответ неправильный"
                self.textbox5.delete(0.0, END)
                self.textbox5.insert(0.0, result)

    def widget3(self):
        Label(self,
              text="Цель рефакторинга - это:",
              font=("Times New Roman", 14), fg="purple"
              ).grid(row=21, column=0, sticky=W)

        Label(self,
              text="Выберите правильный ответ",
              font=("Times New Roman", 12)
              ).grid(row=22, column=0, sticky=W)

        self.otvet9 = StringVar()
        self.otvet9.set(None)
        
        Radiobutton(self,
                   text="Сделать код программы более лёгким для выполнения",
                   font=("Comic Sans MS", 13),
                   variable=self.otvet9,
                   value="Сделать код программы более лёгким для выполнения"
                   ).grid(row=24, column=0, sticky=W)
        
        Radiobutton(self,
                   text="Сделать код программы более лёгким для понимания",
                   font=("Comic Sans MS", 13),
                   variable=self.otvet9,
                   value="Сделать код программы более лёгким для понимания"
                   ).grid(row=25, column=0, sticky=W)
        
        Radiobutton(self,
                   text="Ускорить выполнение программы",
                   font=("Comic Sans MS", 13),
                   variable=self.otvet9,
                   value="Ускорить выполнение программы"
                   ).grid(row=26, column=0, sticky=W)

        self.btn3 = Button(self,
                          text="Ответить",
                          command=self.control3,
                          width=10,
                          height=2,
                          font=("Arial", 12))
        self.btn3.grid(row=27, column=0, sticky=W)

        self.textbox5 = Text(self,
                            width=30,
                            height=2,
                            font=("Times New Roman", 12),
                            fg="blue")
        self.textbox5.grid(row=28, column=0, sticky=W)
#Вопрос№4 с переключателем
        def control4(self):
        p = self.otvet10.get()
        if p == "Сделать код программы более лёгким для понимания":
            result = "Ответ правильный"
        else:
            result = "Ответ неправильный"
        self.textbox6.delete(0.0, END)
        self.textbox6.insert(0.0, result)

    def widget4(self):
        Label(self,
              text="Цель рефакторинга - это (вопрос 4):",
              font=("Times New Roman", 14), fg="green"
              ).grid(row=28, column=0, sticky=W)

        Label(self,
              text="Выберите правильный ответ",
              font=("Times New Roman", 12)
              ).grid(row=29, column=0, sticky=W)

        self.otvet10 = StringVar()
        self.otvet10.set(None)
        
        Radiobutton(self,
                   text="Сделать код программы более лёгким для выполнения",
                   font=("Comic Sans MS", 13),
                   variable=self.otvet10,
                   value="Сделать код программы более лёгким для выполнения"
                   ).grid(row=30, column=0, sticky=W)
        
        Radiobutton(self,
                   text="Сделать код программы более лёгким для понимания",
                   font=("Comic Sans MS", 13),
                   variable=self.otvet10,
                   value="Сделать код программы более лёгким для понимания"
                   ).grid(row=31, column=0, sticky=W)
        
        Radiobutton(self,
                   text="Ускорить выполнение программы",
                   font=("Comic Sans MS", 13),
                   variable=self.otvet10,
                   value="Ускорить выполнение программы"
                   ).grid(row=32, column=0, sticky=W)

        self.btn4 = Button(self,
                          text="Ответить",
                          command=self.control4,  # Исправлено на control4
                          width=10,
                          height=2,
                          font=("Arial", 12))
        self.btn4.grid(row=33, column=0, sticky=W)

        self.textbox6 = Text(self,
                            width=30,
                            height=2,
                            font=("Times New Roman", 12),
                            fg="blue")
        self.textbox6.grid(row=34, column=0, sticky=W)

        
root=Tk()
root.title("Тест по алгоритму")
root.geometry("1920x1080")
app=application(root)
root.mainloop()
