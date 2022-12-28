import sys
n = int(sys.stdin.readline())
a = list(map(int, input().split()))

stack = []
for i in range(n):
    size = 1
    for j in range(i, n-1):
        if a[j+1] >= a[j]:
            size += 1
        else:
            stack.append(size)
            break
for i in range(n):
    size = 1
    for j in range(i, n-1):
        if a[j+1] <= a[j]:
            size += 1
        else:
            stack.append(size)
            break
print(max(stack))
