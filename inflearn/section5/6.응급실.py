from collections import deque
n, m = map(int, input().split())
a = [(pos, val) for pos, val in enumerate((list(map(int, input().split()))))]

cnt = 0
Q = deque(a)

while True:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q):
        Q.append(cur)
    else:
        cnt += 1
        if(cur[0] == m):
            print(cnt)
            break
