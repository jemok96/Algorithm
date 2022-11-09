N, K = map(int, input().split())
a = [*map(int, input().split())]
a.sort()

lt = 1
rt = max(a)
res = 0


def check(len):
    sum = 0
    for x in a:
        if len < x:
            sum += (x-len)
    return sum


while lt <= rt:
    mid = (lt + rt)//2
    if check(mid) >= K:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
