import tkinter as tk

def change_color(event):
    button.config(bg="blue")  # Change the background color to blue when clicked

root = tk.Tk()

# Create a button
button = tk.Button(root, text="Click me!")

# Bind the function to the button's click event
button.bind("<Button-1>", change_color)

button.pack()

root.mainloop()