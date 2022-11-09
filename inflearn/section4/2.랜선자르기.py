k, n = map(int, input().split())
lst = []
largest = 0
res = 0
for _ in range(k):
    x = int(input())
    lst.append(x)
    largest = max(largest, x)
lt = 1
rt = largest


def check(a, mid):
    cnt = 0
    for i in a:
        cnt += (i // mid)
    return cnt


while lt <= rt:
    mid = (lt + rt)//2

    if check(lst, mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
