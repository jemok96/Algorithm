N, K = map(int, input().split())
largest = 0
lst = []
for _ in range(N):
    x = int(input())
    lst.append(x)
    largest = max(largest, x)
lt = 1
rt = largest
lst.sort()


def check(mid):
    cnt = 1
    x = 0
    for i in range(N-1):
        if lst[i+1] - lst[x] >= mid:
            x = i+1
            cnt += 1
    return cnt


res = 0
while lt <= rt:
    mid = (lt + rt)//2
    # print(mid, check(mid))
    if check(mid) >= K:
        res = mid
        lt = mid+1
    else:
        rt = mid - 1
print(res)
