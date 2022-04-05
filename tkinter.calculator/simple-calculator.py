from cgitb import text
import imp
import math
from tkinter import *
from tkinter.font import BOLD

root=Tk()
root.iconbitmap(r'./resources/icon.ico')
root.title("Calculadora Básica")
root.configure(background="#211F22")

#Widget Text

t = Text(root, height=0, width=15, fg="white", padx=10, bg="#211F22", font=(("Lato"), 36))
t.tag_configure("align", justify=RIGHT) #Tag para alinhamento do texto
t.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

#Funções

def click(number): #Insere os numeros
    t.insert(INSERT,number)
    t.tag_add("align", '1.0', END) #Adiciona a tag de alinhamento a sequência de numeros

def clear(): #Limpa a tela
    t.delete('1.0', END)

def plus(): #Realiza soma
    first_number = t.get('1.0', END)
    global f_num
    global math
    math = 1
    f_num = int(first_number)
    t.delete('1.0', END)

def minus(): #Realiza subtração
    first_number = t.get('1.0', END)
    global f_num
    global math
    math = 2
    f_num = int(first_number)
    t.delete('1.0', END)

def mult(): #Realiza multiplicação
    first_number = t.get('1.0', END)
    global f_num
    global math
    math = 3
    f_num = int(first_number)
    t.delete('1.0', END)

def div(): #Realiza divisão
    first_number = t.get('1.0', END)
    global f_num
    global math
    math = 4
    f_num = int(first_number)
    t.delete('1.0', END)

def equal(): #Exibe o resultado
    second_number = t.get('1.0', END)
    t.delete('1.0', END)

    if (math == 1):
        t.insert('1.0', f_num + int(second_number))
    elif (math == 2):
        t.insert('1.0', f_num - int(second_number))
    elif (math == 3):
        t.insert('1.0', f_num * int(second_number))
    elif (math == 4):
        t.insert('1.0', f_num / int(second_number))

    t.tag_add("align", '1.0', END)

#Widget Button

button_padx = 50 #Espaçamento horizontal
button_pady = 15 #Espaçamento vertical
button_font = "Lato 12 bold"

#OBS: Normalmente não é possível passar valores pra função usando command, então usamos o lambda para utilizar funções da forma como conhecemos
b0 = Button(root, text="0", padx=button_padx, pady=button_pady, fg="white", bg="#383B3F", activebackground="#211F22", font=((button_font)), command=lambda : click("0"))
b1 = Button(root, text="1", padx=button_padx, pady=button_pady, fg="white", bg="#383B3F", activebackground="#211F22", font=((button_font)), command=lambda : click(1))
b2 = Button(root, text="2", padx=button_padx, pady=button_pady, fg="white", bg="#383B3F", activebackground="#211F22", font=((button_font)), command=lambda : click(2))
b3 = Button(root, text="3", padx=button_padx, pady=button_pady, fg="white", bg="#383B3F", activebackground="#211F22", font=((button_font)), command=lambda : click(3))
b4 = Button(root, text="4", padx=button_padx, pady=button_pady, fg="white", bg="#383B3F", activebackground="#211F22", font=((button_font)), command=lambda : click(4))
b5 = Button(root, text="5", padx=button_padx, pady=button_pady, fg="white", bg="#383B3F", activebackground="#211F22", font=((button_font)), command=lambda : click(5))
b6 = Button(root, text="6", padx=button_padx, pady=button_pady, fg="white", bg="#383B3F", activebackground="#211F22", font=((button_font)), command=lambda : click(6))
b7 = Button(root, text="7", padx=button_padx, pady=button_pady, fg="white", bg="#383B3F", activebackground="#211F22", font=((button_font)), command=lambda : click(7))
b8 = Button(root, text="8", padx=button_padx, pady=button_pady, fg="white", bg="#383B3F", activebackground="#211F22", font=((button_font)), command=lambda : click(8))
b9 = Button(root, text="9", padx=button_padx, pady=button_pady, fg="white", bg="#383B3F", activebackground="#211F22", font=((button_font)), command=lambda : click(9))

bplus = Button(root, text="+", padx=button_padx, pady=button_pady, fg="white", bg="#383B3F", activebackground="#211F22", font=((button_font)), command=plus)
bminus = Button(root, text="-", padx=button_padx, pady=button_pady, fg="white", bg="#383B3F", activebackground="#211F22", font=((button_font)), command=minus)
bmult = Button(root, text="X", padx=button_padx, pady=button_pady, fg="white", bg="#383B3F", activebackground="#211F22", font=((button_font)), command=mult)
bdiv = Button(root, text="/", padx=button_padx, pady=button_pady, fg="white", bg="#383B3F", activebackground="#211F22", font=((button_font)), command=div)
bclear = Button(root, text="C", padx=button_padx, pady=button_pady, fg="white", bg="#383B3F", activebackground="#211F22", font=((button_font)), command=clear)
bequal = Button(root, text="=", padx=button_padx, pady=button_pady, fg="white", bg="#505A61", activebackground="#211F22", font=((button_font)), command=equal)

#Posicionamento dos Buttons

bclear.grid(row=4, column=0, padx=5, pady=5)
b0.grid(row=4, column=1, padx=5, pady=5)
bequal.grid(row=4, column=2, padx=5, pady=5)
bplus.grid(row=4, column=3, padx=5, pady=5)

b1.grid(row=3, column=0, padx=5, pady=5)
b2.grid(row=3, column=1, padx=5, pady=5)
b3.grid(row=3, column=2, padx=5, pady=5)
bminus.grid(row=3, column=3, padx=5, pady=5)

b4.grid(row=2, column=0, padx=5, pady=5)
b5.grid(row=2, column=1, padx=5, pady=5)
b6.grid(row=2, column=2, padx=5, pady=5)
bmult.grid(row=2, column=3, padx=5, pady=5)

b7.grid(row=1, column=0, padx=5, pady=5)
b8.grid(row=1, column=1, padx=5, pady=5)
b9.grid(row=1, column=2, padx=5, pady=5)
bdiv.grid(row=1, column=3, padx=5, pady=5)


root.mainloop()