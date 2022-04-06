from tkinter import *
import glob
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap(r'./resources/image.ico')
root.configure(background="#211F22")

#General Customization Variables
button_font = "Lato 12 bold"
fg_color = "white"
bg_color = "#383B3F"
activebg_color = "#211F22"

file_list = glob.glob(r'./images/*.png') #Add to list all .png files path of a specific directory. Use print(file_list) to understand.

img = ImageTk.PhotoImage(Image.open(file_list[0])) #Associates the first image of file_list list to img variable

#Label Widget
label = Label(bg=bg_color, bd=0, image=img) #Show the image in a label widget
status = Label(root, bg=activebg_color, fg=fg_color, bd=0, anchor=E,
               text="Image 1 of " + str(len(file_list))) #Show the current image number and total number of images

label.grid(row=0, column=2, columnspan=3)
status.grid(row=1, column=0, columnspan=6, sticky=W+E)

#Functions
def controller(img_number): #Function to control the exhibition of images
    global img_control #Controls the index of the images
    global label
    global btn_next
    global btn_back

    label.grid_forget() #Prevents images overlaping

    img_control = ImageTk.PhotoImage(Image.open(file_list[img_number])) #Associates the image of file_list list in current index to img_control variable
    label = Label(bg=bg_color, bd=0, image=img_control) #Show the image in a label widget

    #Every time press "Next" button, add 1 to index. So this permits we advance throug the file_list list and show the next image in the label before
    btn_next = Button(root, text=">>", padx=btn_padx, pady=btn_pady, fg=fg_color, bg=bg_color,
                      activebackground=activebg_color, activeforeground=fg_color, bd=0,
                      font=((button_font)), command=lambda: controller(img_number + 1))

    #Every time press "Back" button, subtracts 1 to index. So this permits we go back throug the file_list list and show the previous image in the label before
    btn_back = Button(root, text="<<", padx=btn_padx, pady=btn_pady, fg=fg_color, bg=bg_color,
                      activebackground=activebg_color, activeforeground=fg_color, bd=0,
                      font=((button_font)), command=lambda: controller(img_number - 1))

    if img_number == len(file_list) - 1: #If index equals the size of file_list list...
        btn_next = Button(root, text=">>", padx=btn_padx, pady=btn_pady, fg=fg_color, bg=bg_color,
                          activebackground=activebg_color, activeforeground=fg_color, bd=0,
                          font=((button_font)), state=DISABLED) #Disable the "Next" button

    elif img_number == 0: #If index equals 0...
        btn_back = Button(root, text="<<", padx=btn_padx, pady=btn_pady, fg=fg_color, bg=bg_color,
                          activebackground=activebg_color, activeforeground=fg_color, bd=0,
                          font=((button_font)), state=DISABLED) #Disable the "Back" button

    btn_back.grid(row=0, column=0)
    btn_next.grid(row=0, column=5)

    status = Label(root, bg=activebg_color, fg=fg_color, bd=0, anchor=E,
                   text="Image " + str(img_number + 1) + " of " + str(len(file_list)))  # Show the current image number and total number of images

    label.grid(row=0, column=2, columnspan=3)
    status.grid(row=1, column=0, columnspan=6, sticky=W + E)

#Button Widget
btn_padx = 15
btn_pady = 147

btn_back = Button(root, text="<<", padx=btn_padx, pady=btn_pady, fg=fg_color, bg=bg_color,
                  activebackground=activebg_color, activeforeground= fg_color, bd=0,
                  font=((button_font)), state=DISABLED)
btn_next = Button(root, text=">>", padx=btn_padx, pady=btn_pady, fg=fg_color, bg=bg_color,
                  activebackground=activebg_color, activeforeground= fg_color, bd=0,
                  font=((button_font)), command=lambda: controller(1))

#Button Positioning
btn_back.grid(row=0, column=0)
btn_next.grid(row=0, column=5)


root.mainloop()