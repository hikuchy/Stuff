from tkinter import *

file = open("ter.txt","r")
c = file.read(5)
print(c)
file.close()
file = open("ter.txt","w")
file.write("sgshssh")
file.close()







































