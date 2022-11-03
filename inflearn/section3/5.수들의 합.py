N, M = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < M:
        if rt < N:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == M:
        cnt += 1
        lt = rt-1
        tot = a[lt]
    else:
        tot

print(cnt)
