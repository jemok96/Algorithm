
n, m = map(int, input().split())
Line = []
for _ in range(n):
    Line.append(int(input()))
Line.sort()


lt = 1
rt = Line[n-1]
res = 0


def check(mid):
    cnt = 1
    ep = Line[0]
    for i in Line:
        if i - ep >= mid:
            ep = i
            cnt += 1
    return cnt


while lt <= rt:
    mid = (lt+rt)//2
    if check(mid) >= m:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)
