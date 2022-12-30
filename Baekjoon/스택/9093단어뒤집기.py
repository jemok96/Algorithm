n = int(input())
for _ in range(n):
    stack = []
    s = input()
    s += " "
    for i in s:
        if(i != " "):
            stack.append(i)
        else:
            while stack:
                st = stack.pop()
                print(st, end="")
            print(" ", end="")
