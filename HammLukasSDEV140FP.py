from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image



root = Tk()
root.title("SportsWRLD Login Page")
root.geometry("1280x720")
root.configure(bg="#c2a329")
root.iconbitmap("C:/Users/ta_fi/PycharmProjects/HammLukasFinalProjectSDEV140/venv/Scripts/sports.ico")
#basic root functions inclouding: window title, window size, background color, and icon

e = Entry(root, width=28, bg="white", fg="black", font="Arial", borderwidth=5)
e.place(x=515, y=160)
enter_one = Label(root, text="Username: ", bg="#7a7561", fg="white" ,font="Helvetica 10")
enter_one.place(x=440, y=164)
e_two = Entry(root, width=28, bg="white", fg="black", font="Arial", borderwidth=5)
e_two.place(x=515, y=195)
enter_two = Label(root, text="Password: ", bg="#7a7561", fg="white" ,font="Helvetica 10")
enter_two.place(x=440, y=198)
#two uses of entry to "simulate" a login page screen
#I used labels instead of e.insert b/c I believe it makes the window more clean, even though it is very, very basic

basic_B = Label(root, text="Welcome to SportsWRLD"
                           "\nHome of the Best Sports Jerseys", bg="#7a7561", fg="white", font="Helvetica 25 bold" )
basic_B.place(x=400, y=50)
basic_C = Label(root, text="Please login to your account to continue", bg="#7a7561", fg="white", font="Helvetica 8 bold")
basic_C.place(x=525, y=130)
#basics of root window, label, window size, window color, etc.
#example login button to "login" into SportsWRLD page that takes you to second window

button_exit = Button(root, text="EXIT SportsWRLD", command=root.quit)
button_exit.place(x=600, y=650)
#exit button for login root window


my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/ta_fi/PycharmProjects/HammLukasFinalProjectSDEV140/venv/Scripts/bob.png"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/ta_fi/PycharmProjects/HammLukasFinalProjectSDEV140/venv/Scripts/marc.png"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/ta_fi/PycharmProjects/HammLukasFinalProjectSDEV140/venv/Scripts/mcgwire.png"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/ta_fi/PycharmProjects/HammLukasFinalProjectSDEV140/venv/Scripts/tatum.png"))

image_list = [my_img1, my_img2, my_img3, my_img4]
#array of images
my_label = Label(image=my_img1)
my_label2 = Label(image=my_img2)
my_label3 = Label(image=my_img3)
my_label4 = Label(image=my_img4)
#using labels to display images

my_label.place(x=100, y=200 )
my_label2.place(x=100, y=400)
my_label3.place(x=850, y=150)
my_label4.place(x=850, y=400)
#images placed inside of root window to show what SportsWRLD shop has to offer customers

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
        top.iconbitmap("C:/Users/ta_fi/PycharmProjects/HammLukasFinalProjectSDEV140/venv/Scripts/sports.ico")
        #basics of second window
        counter +=1

        l_Ac = Label(top, text="Hello "  + e.get() + "\nWelcome back to SportsWRLD!" + "\nWe are currently closed for "
                                                                                       "\nIvy Tech Graduation! ", font="Helvetica 20 bold")
        l_Ac.place(x=350, y=50)


        button_exit = Button(top, text="Exit SportsWRLD Shop", command=top.quit, fg="white", bg="red", font="Arial 8 bold")
        button_exit.place(x=500, y=15)



    else:
        messagebox.showinfo("Error", "You have already logged in on another window")

#button to login into SportsWRLD
new_button = Button(root, text="Login", command=new_W)
new_button.place(x=625, y=250)




root.mainloop()
