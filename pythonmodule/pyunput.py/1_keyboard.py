from pynput import keyboard
def press(key):
    print("Key pressed:", key)
def release(key):
    if key== keyboard.Key.esc:
        return False
print("Press keys. Press ESC to stop.")
with keyboard.Listener(on_press=press, on_release=release) as listener:
    listener.join()