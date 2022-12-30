# s = list(input())
# print(ord('a'))
# print(ord('z'))
# print(ord('A'))
# print(ord('Z'))

# for x in s:
#     if ord(x) >= 97 and ord(x) <= 122:  # 소문자일떄
#         if ord(x)+13 > 122:
#             x = 97+(ord(x)+13-122)
#         else:
#             x = 97+13
#         print(chr(x), end="")
#     elif ord(x) >= 65 and ord(x) <= 90:
#         if ord(x)+13 > 90:
#             x = 65+(ord(x)+13-90)
#         else:
#             x = 65+13
#         print(chr(x), end="")
#     elif x == " ":
#         print(" ", end="")

lst = [[0]*5 for _ in range(10)]
print(lst)
