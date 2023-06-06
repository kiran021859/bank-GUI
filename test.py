from tkinter import *
from PIL import ImageTk, Image

def hello():
    print("Hello, World!")

Home = Tk()

# Open and resize the image
image = Image.open("blue-glossy-button.png")
image = image.resize((200, 80))

# Convert the image to Tkinter-compatible format
photo = ImageTk.PhotoImage(image)

# Create a button with the image as the background and text
button = Button(Home, image=photo, command=hello, text="Hello, World!", compound="center", borderwidth=0)
button.grid(row=6, sticky=N, pady=10)

Home.mainloop()