s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if(s[i] == '('):
        stack.append('(')
    else:
        if(s[i-1] == '('):
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(stack)
print(cnt)
# (((()(()())) 2/16 (())()))(()())
