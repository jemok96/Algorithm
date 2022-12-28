import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    s = sys.stdin.readline().split()
    com = s[0]
    if com == 'push':
        stack.append(s[1])
    elif com == 'empty':
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
    elif com == 'size':
        print(len(stack))
    elif com == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif com == 'pop':
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack.pop())
