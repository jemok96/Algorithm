from collections import deque
n, k = map(int, input().split())
stack = list(range(1, n+1))
stack = deque(stack)
result = []
while stack:
    for i in range(k-1):
        stack.append(stack.popleft())
    result.append(stack.popleft())

print(str(result).replace('[', '<').replace(']', '>'))
