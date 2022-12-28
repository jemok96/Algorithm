import sys
stack = list(sys.stdin.readline().strip())  # 입력값 배열
n = int(sys.stdin.readline())
tmp = []  # tmp배열

for _ in range(n):
    com = sys.stdin.readline().split()
    if(com[0] == 'L'):
        if stack:
            tmp.append(stack.pop())
    elif com[0] == 'P':
        stack.append(com[1])
    elif com[0] == 'B':
        if stack:
            stack.pop()
    else:
        if tmp:
            stack.append(tmp.pop())
if tmp:
    while tmp:
        stack.append(tmp.pop())
for x in stack:
    print(x, end="")
