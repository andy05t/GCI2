from tkinter import *
import webbrowser
import tkinter.messagebox

def opengit():
    webbrowser.open("https://github.com")
def open_news():
    webbrowser.open("https://www.bbc.co.uk/news")
def pacman():
    webbrowser.open("https://elgoog.im/pacman/")

root = Tk()

root.title("My program helping you to automate 3 tasks")
root.configure(background = "white")

top_frame = Frame(root)
top_frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack(side = BOTTOM)

label1 = Label(top_frame, text = "Hello there user! Please choose one of the options...", fg = "Blue", bg = "yellow")
label1.pack(side = TOP, expand = False, fill = X)

b1 = Button(top_frame, text = "Click here to access Github!", bg = "red", command = opengit)
b1.pack(side = LEFT, padx = 2, pady = 2)

b2 = Button(top_frame, text = "Click here to open the latest BBC News!", bg = "green", command = open_news)
b2.pack(side = LEFT, padx = 2, pady = 2)

b3 = Button(top_frame, text = "Click here to play Pacman!", bg = "magenta", command = pacman)
b3.pack(side = LEFT, padx = 2, pady = 2)


photo = PhotoImage(file = "enjoy.png")
l = Label(bottom_frame, image = photo, bg = "white")
l.pack()

root.mainloop()


