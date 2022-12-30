s = list(input())
for i in range(97, 123):
    count = s.count(chr(i))
    print(count, end=" ")
