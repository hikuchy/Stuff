#zadacha
from tkinter import *
from math import *
class application(Frame):
    def __init__(self, fr):
        super(application, self).__init__(fr)
        self.grid()
        self.widget()
#Нахождение квадратного уравнения
    def quadro(self):
        a=int(self.a.get())
        b=int(self.b.get())
        c=int(self.c.get())
        if a==0:
            if b==0:
                if c==0:
                    l="x-любое число"
                #elif c!=0
                print("решения нет")
            elif b!=0:
                if c==0:
                    print("x=0")
                elif c!=0:
                    print("x=-c/b")
        if a!=0:
            if b==0:
                if c==0:
                    print("x=0")
                #if c!=0:
                    
        self.rez.delete(0.0,END)
        self.rez.insert(0.0,l)     
#Надпись
    def widget(self):
        self.lbl=Label(self,text="Число а")
        self.lbl.grid(row=0,column=1)
#Число а       
        self.a=Entry(self)
        self.a.grid(row=1,column=1)
#Надпись
        self.lbl=Label(self,text="Число b")
        self.lbl.grid(row=2,column=1)
#Число b
        self.b=Entry(self)
        self.b.grid(row=3,column=1)
#Надпись
        self.lbl=Label(self,text="Число c")
        self.lbl.grid(row=4,column=1)
#Число с
        self.c=Entry(self)
        self.c.grid(row=5,column=1)
#Надпись 
        self.lbl=Label(self,text="Квадатное уравнение a*x^2+b*x+c")
        self.lbl.grid(row=5,column=2)
#Текстовое поле для квадратного уравнения
        #self.l=Entry(self)
        #self.l.grid(row=6,column=2)
        self.btn = Button(self,
                         text="решить",
                         command=self.quadro,
                         width=10,
                         height=2,
                         font=("Arial", 12))
        self.btn.grid(row=7, column=1
                      ,)
        self.rez=Text(self,width=20,height=3)
        self.rez.grid(row=8,column=2)


root=Tk()
root.title("Нахождение корней")
root.geometry("800x600") 
app=application(root)
root.mainloop()
