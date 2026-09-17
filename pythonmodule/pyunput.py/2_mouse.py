from pynput import mouse

def click(x, y, button, pressed):
    if pressed:
        print("Mouse clicked:", x, y, button)

print("Click the mouse. Close the program when finished.")

with mouse.Listener(on_click=click) as listener:
    listener.join()
