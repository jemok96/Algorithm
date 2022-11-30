from collections import deque

N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = deque(a)
cnt = 0

# while a:
#     if len(a) == 1:
#         cnt += 1
#         break
#     if a[0] + a[-1] > M:
#         a.pop()
#         cnt += 1
#     else:
#         a.pop(0)
#         a.pop()
#         cnt += 1
# print(cnt)

while a:
    if len(a) == 1:
        cnt += 1
        break
    if a[0] + a[-1] > M:
        a.pop()
        cnt += 1
    else:
        a.popleft()
        a.pop()
        cnt += 1
print(cnt)
