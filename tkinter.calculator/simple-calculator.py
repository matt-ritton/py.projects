from cgitb import text
import imp
import math
from tkinter import *
from tkinter.font import BOLD

root=Tk()
root.iconbitmap(r'./resources/icon.ico')
root.title("Simple Calculator")
root.configure(background="#211F22")

#Text Widget

t = Text(root, height=0, width=15, fg="white", padx=10, bg="#211F22", font=(("Lato"), 36))
t.tag_configure("align", justify=RIGHT) #Text align tag
t.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

#Functions

def click(number): #Number insertion
    t.insert(INSERT,number)
    t.tag_add("align", '1.0', END) #Add alignment tag in entered numbers

def clear(): #Clear function
    t.delete('1.0', END)

def plus(): #Sum function
    first_number = t.get('1.0', END)
    global f_num
    global math
    math = 1
    f_num = int(first_number)
    t.delete('1.0', END)

def minus(): #Subtraction function
    first_number = t.get('1.0', END)
    global f_num
    global math
    math = 2
    f_num = int(first_number)
    t.delete('1.0', END)

def mult(): #Multiplication function
    first_number = t.get('1.0', END)
    global f_num
    global math
    math = 3
    f_num = int(first_number)
    t.delete('1.0', END)

def div(): #Division function
    first_number = t.get('1.0', END)
    global f_num
    global math
    math = 4
    f_num = int(first_number)
    t.delete('1.0', END)

def equal(): #Show the results in screen
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

#Button Widget

button_padx = 50 #Horizontal padding
button_pady = 15 #Vertical padding
button_font = "Lato 12 bold"
fg_color = "white"
bg_color = "#383B3F"
activebg_color = "#211F22"

#PS: Normally it's not possible to pass values to the function using command, so we use lambda to use functions as we know them.
b0 = Button(root, text="0", padx=button_padx, pady=button_pady, fg=fg_color, bg=bg_color, activebackground=activebg_color, font=((button_font)), command=lambda : click("0"))
b1 = Button(root, text="1", padx=button_padx, pady=button_pady, fg=fg_color, bg=bg_color, activebackground=activebg_color, font=((button_font)), command=lambda : click(1))
b2 = Button(root, text="2", padx=button_padx, pady=button_pady, fg=fg_color, bg=bg_color, activebackground=activebg_color, font=((button_font)), command=lambda : click(2))
b3 = Button(root, text="3", padx=button_padx, pady=button_pady, fg=fg_color, bg=bg_color, activebackground=activebg_color, font=((button_font)), command=lambda : click(3))
b4 = Button(root, text="4", padx=button_padx, pady=button_pady, fg=fg_color, bg=bg_color, activebackground=activebg_color, font=((button_font)), command=lambda : click(4))
b5 = Button(root, text="5", padx=button_padx, pady=button_pady, fg=fg_color, bg=bg_color, activebackground=activebg_color, font=((button_font)), command=lambda : click(5))
b6 = Button(root, text="6", padx=button_padx, pady=button_pady, fg=fg_color, bg=bg_color, activebackground=activebg_color, font=((button_font)), command=lambda : click(6))
b7 = Button(root, text="7", padx=button_padx, pady=button_pady, fg=fg_color, bg=bg_color, activebackground=activebg_color, font=((button_font)), command=lambda : click(7))
b8 = Button(root, text="8", padx=button_padx, pady=button_pady, fg=fg_color, bg=bg_color, activebackground=activebg_color, font=((button_font)), command=lambda : click(8))
b9 = Button(root, text="9", padx=button_padx, pady=button_pady, fg=fg_color, bg=bg_color, activebackground=activebg_color, font=((button_font)), command=lambda : click(9))

bplus = Button(root, text="+", padx=button_padx, pady=button_pady, fg=fg_color, bg=bg_color, activebackground=activebg_color, font=((button_font)), command=plus)
bminus = Button(root, text="-", padx=button_padx, pady=button_pady, fg=fg_color, bg=bg_color, activebackground=activebg_color, font=((button_font)), command=minus)
bmult = Button(root, text="X", padx=button_padx, pady=button_pady, fg=fg_color, bg=bg_color, activebackground=activebg_color, font=((button_font)), command=mult)
bdiv = Button(root, text="/", padx=button_padx, pady=button_pady, fg=fg_color, bg=bg_color, activebackground=activebg_color, font=((button_font)), command=div)
bclear = Button(root, text="C", padx=button_padx, pady=button_pady, fg=fg_color, bg=bg_color, activebackground=activebg_color, font=((button_font)), command=clear)
bequal = Button(root, text="=", padx=button_padx, pady=button_pady, fg=fg_color, bg="#505A61", activebackground=activebg_color, font=((button_font)), command=equal)

#Buttons Positioning

btn_padx = 5
btn_pady = 5

bclear.grid(row=4, column=0, padx=btn_padx, pady=btn_pady)
b0.grid(row=4, column=1, padx=btn_padx, pady=btn_pady)
bequal.grid(row=4, column=2, padx=btn_padx, pady=btn_pady)
bplus.grid(row=4, column=3, padx=btn_padx, pady=btn_pady)

b1.grid(row=3, column=0, padx=btn_padx, pady=btn_pady)
b2.grid(row=3, column=1, padx=btn_padx, pady=btn_pady)
b3.grid(row=3, column=2, padx=btn_padx, pady=btn_pady)
bminus.grid(row=3, column=3, padx=btn_padx, pady=btn_pady)

b4.grid(row=2, column=0, padx=btn_padx, pady=btn_pady)
b5.grid(row=2, column=1, padx=btn_padx, pady=btn_pady)
b6.grid(row=2, column=2, padx=btn_padx, pady=btn_pady)
bmult.grid(row=2, column=3, padx=btn_padx, pady=btn_pady)

b7.grid(row=1, column=0, padx=btn_padx, pady=btn_pady)
b8.grid(row=1, column=1, padx=btn_padx, pady=btn_pady)
b9.grid(row=1, column=2, padx=btn_padx, pady=btn_pady)
bdiv.grid(row=1, column=3, padx=btn_padx, pady=btn_pady)


root.mainloop()