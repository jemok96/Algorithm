import sys
n = int(sys.stdin.readline())
for _ in range(n):
    stack = []
    s = sys.stdin.readline()
    for x in s:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(x)
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
