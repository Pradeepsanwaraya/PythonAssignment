import customtkinter as ctk

def show():
    label.configure(text="Button Clicked")

root = ctk.CTk()
root.title("Custom Button")
root.geometry("500x300")

label = ctk.CTkLabel(root, text="Click the button")
label.pack(pady=30)

button = ctk.CTkButton(root, text="Click Me", command=show)
button.pack()

root.mainloop()
