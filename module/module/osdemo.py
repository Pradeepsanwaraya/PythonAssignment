import os
print("Current folder:",os.getcwd())
print("Files and folders:",os.listdir())
print("test folder exists:",os.path.exists("test"))
if not os.path.exists("test"):
    os.mkdir("test")
print("Is folder:",os.path.isdir("test"))
print("Is file:",os.path.isfile("abc.txt"))
print("File size:",os.path.getsize("abc.txt"))
path=os.path.join("test","abc.txt")
print("Path:",path)
# os.rmdir("test")