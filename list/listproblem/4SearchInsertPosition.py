l = [1,3,5,6]
target = 2

for i in range(len(l)):
    if l[i] >= target:
        index = i
        l[i]=target
        break
else:
    index = len(l)   
print(l)