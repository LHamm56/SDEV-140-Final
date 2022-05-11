from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk



root = Tk()
root.title("SportsWRLD Login Page")
root.geometry("1280x720")
root.configure(bg="#c2a329")

#basic root functions, still trying to figure out how to use root.iconbitmap to import a .ico image for my window icon






e = Entry(root, width=28, bg="white", fg="black", font="Arial", borderwidth=5)
e.place(x=515, y=150)
enter_one = Label(root, text="Username: ", bg="#7a7561", fg="white" ,font="Helvetica 10")
enter_one.place(x=440, y=154)
e_two = Entry(root, width=28, bg="white", fg="black", font="Arial", borderwidth=5)
e_two.place(x=515, y=185)
enter_two = Label(root, text="Password: ", bg="#7a7561", fg="white" ,font="Helvetica 10")
enter_two.place(x=440, y=188)
#two uses of entry to "simulate" a login page screen
#I used labels instead of e.insert b/c I believe it makes the window more clean, even though it is very, very basic

basic_B = Label(root, text="Welcome to SportsWRLD", bg="#7a7561", fg="white", font="Helvetica 25 bold" )
basic_B.place(x=450, y=50)
basic_C = Label(root, text="Please login to your account to continue", bg="#7a7561", fg="white", font="Helvetica 10 bold")
basic_C.place(x=515, y=100)
#basics of root window, label, window size, window color, etc.
#example login button to "login" into SportsWRLD page that takes you to second window

button_exit = Button(root, text="EXIT SportsWRLD", command=root.quit)
button_exit.place(x=600, y=650)
#exit button for login root window






#class for second window
class new_Window():

    global counter
    counter = 1

def new_W():
    global counter

    if counter < 4:
        top = Toplevel()
        top.geometry("1080x1024")
        top.title("SportsWRLD Main Page")
        top.configure(bg="#2eb352")
        #basics of second window
        counter +=1

        l_Ac = Label(top, text="Hello "  + e.get() + "\nWelcome back to SportsWRLD!" + "\nLook at our new drops!", font="Helvetica 20 bold")
        l_Ac.place(x=350, y=50)

        button_back = Button(top, text="<<", width=10, bg="black", fg="white")
        button_back.place(x=325, y=625)
        button_exit = Button(top, text="Exit SportsWRLD Shop", command=top.quit, fg="white", bg="red", font="Arial 8 bold")
        button_exit.place(x=500, y=15)
        button_forward = Button(top, text=">>", width=10, bg="black", fg="white" )
        button_forward.place(x=725, y=625)
        #start of a WIP image viewer I am trying to run through the second page
        #problems I am running into: getting images into python, trying to use Pillow or normal Tkinter for images, image errors/ directory issues. 



    else:
        messagebox.showinfo("Error", "You have already logged in on another window")














#WIP second window w/ button from root window to open
new_button = Button(root, text="Login", command=new_W)
new_button.place(x=625, y=250)




root.mainloop()
