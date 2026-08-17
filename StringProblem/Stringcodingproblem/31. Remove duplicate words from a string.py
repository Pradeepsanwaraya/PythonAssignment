s = input("enter a string").split()
done = ""
for i in s:
    if i not in done.split():
        done = done + i + " "

print(done)