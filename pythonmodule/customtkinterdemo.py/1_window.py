import customtkinter as ctk

ctk.set_appearance_mode("System")

root = ctk.CTk()
root.title("Custom Tkinter")
root.geometry("500x300")

label = ctk.CTkLabel(root, text="Hello CustomTkinter")
label.pack(pady=50)

root.mainloop()
