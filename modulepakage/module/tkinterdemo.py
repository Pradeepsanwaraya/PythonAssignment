# import tkinter → Tkinter ko laaya
# Tk() → window banayi
# title() → window ka naam
# geometry() → window ka size
# mainloop() → window ko running rakhta hai
import tkinter
window=tkinter.Tk()
window.title("window")
window.geometry("500x4000")
label=tkinter.Label(window,text="Hello Bhai")

button=tkinter.Button(window,text="Click Me",command="click")
button.pack()
label.pack()
window.mainloop()
