N, K = map(int, input().split())
lst = []
largest = 0
res = 0
for _ in range(N):
    x = int(input())
    lst.append(x)
    largest = max(largest, x)
lt = 0
rt = largest


def check(mid):
    cnt = 0
    for x in lst:
        cnt += (x//mid)
    return cnt


while lt <= rt:
    mid = (lt+rt) // 2
    if check(mid) >= K:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
