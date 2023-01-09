a = input()
stack = []

for x in a:
    if x.isdecimal():
        stack.append(x)
    else:
        if x == '/':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a/b)
        elif x == '*':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a*b)
        elif x == '+':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a+b)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b-a)

print(stack[0])
