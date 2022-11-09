N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = a[0]
rt = a[-1]
cnt = 0

while lt <= rt:
    mid = (lt+rt) // 2
    if mid > M:
        rt = mid - 1
    elif mid < M:
        lt = mid+1

    elif mid == M:
        print(a.index(mid)+1)
        break
