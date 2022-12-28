import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
for _ in range(n):
    s = sys.stdin.readline().split()
    com = s[0]
    if com == 'push':
        queue.append(s[1])
    elif com == 'size':
        print(len(queue))
    elif com == 'empty':
        if(len(queue) == 0):
            print(1)
        else:
            print(0)
    elif com == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif com == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif com == 'pop':
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue.popleft())
