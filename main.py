from tkinter import *
from tkinter import ttk
import os

root = Tk()

# Making window align to the center
height = 430
width = 530
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root.config(background="#fefdff")

welcome_label = Label(text="CiTi BANK", bg="#ffffff", font=("Trebuchet Ms", 25, "bold"), fg="#3f3960")
welcome_label.place(x=180, y=25)

# Load the image for bg_label
image = PhotoImage(file="C:\\Users\\Kiran Isaacs\\Desktop\\banking app1\\images.png")
bg_label = Label(root, image=image, bd=0, highlightthickness=0)
bg_label.place(x=190, y=125)

progress_label = Label(root, text="Loading...", font=("Trebuchet Ms", 13, "bold"), fg="#3f3960", bg="#fefdff")
progress_label.place(x=195, y=280)

progress_style = ttk.Style()
progress_style.theme_use('clam')
progress_style.configure("red.Horizontal.TProgressbar", background="#457686")

progress = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate', style="red.Horizontal.TProgressbar")
progress.place(x=60, y=320)

def top():
    root.withdraw()
    os.system("python index.py")
    root.destroy()

def load(i=0):
    if i <= 100:
        txt = 'Loading...' + str(i) + '%'
        progress_label.config(text=txt)
        progress['value'] = i
        progress.after(250, load, i+10)
    else:
        top()

load()

root.resizable(False, False)
root.mainloop()
