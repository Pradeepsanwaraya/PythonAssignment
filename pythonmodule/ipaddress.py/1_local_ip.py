import socket

name = socket.gethostname()
ip = socket.gethostbyname(name)

print("Computer Name:", name)
print("IP Address:", ip)
