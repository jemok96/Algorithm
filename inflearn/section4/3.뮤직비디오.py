n, m = map(int, input().split())
a = list(map(int, input().split()))

res = 0
lt = 9
rt = sum(a)


def check(mid):
    cnt = 1
    sum = 0
    for x in a:
        if sum+x <= mid:
            sum += x
        else:
            cnt += 1
            sum = x
    return cnt


while lt <= rt:
    mid = (lt + rt)//2
    # print(lt, rt, mid, res)
    if check(mid) <= m:
        res = mid
        rt = mid - 1

    else:
        lt = mid + 1
print(res)
