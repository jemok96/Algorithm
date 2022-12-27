num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []

for x in num:
    while stack and x > stack[-1] and m > 0:
        stack.pop()
        m -= 1
    stack.append(x)

if(m > 0):
    stack = stack[:-m]
for x in stack:
    print(x, end="")
