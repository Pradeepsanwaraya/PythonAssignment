import tkinter as tk

def show():
    label.config(text="Button Clicked")

root = tk.Tk()
root.title("Button Example")

label = tk.Label(root, text="Click the button")
label.pack()

button = tk.Button(root, text="Click Me", command=show)
button.pack()

root.mainloop()
