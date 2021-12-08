from tkinter import *
# from tkinter.ttk import *
from PIL import Image, ImageTk
import googletrans
from googletrans import Translator
translator = Translator()

# create the main window
root = Tk()
root.title('Translator App - Nam Phan')
root.geometry("500x630")
root.iconbitmap('logo.ico')

load = Image.open('background.png')
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0, y=0)

# create Translator Text Header
name = Label(root, text="Translator", fg="#FFFFFF", bd=0, bg="#03152D")
name.config(font=("Transformers Movie", 30))
name.pack(pady=10)

# create top box
top_box = Text(root, width=28, height=8, font=("ROBOTO", 16))
top_box.pack(pady=20)

# create button under the top box
button_frame = Frame(root).pack(side=BOTTOM)


def clear():
    top_box.delete(1.0, END)
    bottom_box.delete(1.0, END)


def translate():
    INPUT = top_box.get(1.0, END)
    print(INPUT)
    t = Translator()
    a = t.translate(INPUT, src="en", dest="vi")
    b = a.text
    bottom_box.insert(END, b)


clear_button = Button(button_frame, text="Clear Text", font=(
    ("Arial"), 10, 'bold'), bg="#303030", fg="#FFFFFF", command=clear)
clear_button.place(x=150, y=310)
trans_button = Button(button_frame, text="Translate", font=(
    ("Arial"), 10, 'bold'), bg="#303030", fg="#FFFFFF", command=translate)
trans_button.place(x=290, y=310)

# create bottom box
bottom_box = Text(root, width=28, height=8, font=("ROBOTO", 16))
bottom_box.pack(pady=50)


root.mainloop()
