# s = input("enter a string")
# s2 = input("enter a string2")

# if len(s) != len(s2):
#     print(False)

# else:
#     temp = s + s

#     flag = False

#     for i in range(len(s)):

#         # Har new starting position par
#         # maan rahe hain ki match ho jayega
#         match = True

#         for j in range(len(s2)):

#             # i = temp me starting position
#             # j = s2 ka current character
#             if temp[i+j] != s2[j]:
#                 match = False
#                 break

#         if match:
#             flag = True
#             break

#     print(flag)
x = [1, 2, [3, 4]]
y = x[:]
y[2].append(5)

print(x, y, x is y)