import os
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


root = Tk()
root.title("SportsWRLD")
root.geometry("1280x720")
root.configure(bg="#c2a329")
basic_B = Label(root, text="Welcome to SportsWRLD", bg="#7a7561", fg="white", font="Helvetica 18 bold" )
basic_B.place(x=500, y=50)
#basics of root window, label, window size, window color, etc.

button_exit = Button(root, text="Exit Program", command=root.quit)
button_exit.place(x=100, y=0)
#exit button


global counter
counter = 1

def new_W():
    global counter

    if counter < 4:
        top = Toplevel()
        top.geometry("1080x1024")
        top.title("Secret Window")

        l_Ab = Label(top, text="You found it!", font="Helvetica 20")
        l_Ab.place(x=100, y=50)

        counter +=1

    else:
        messagebox.showinfo("Error", "You already found the secret window!")

#WIP second window w/ button from root window to open
new_button = Button(root, text="SECRET!", command=new_W)
new_button.place(x=50, y=50)

root.mainloop()
