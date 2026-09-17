import tkinter as tk 
window=tk.Tk()
window.title("My App")
window.geometry("400x300")
label=tk.Label(window,text="Enter your name")
label.pack()
entry=tk.Entry(window)
entry.pack()
def hello():
    name=entry.get()
    label.config(text="Hello "+name)
button=tk.Button(window,text="Click Me",command=hello)
button.pack()
window.mainloop()