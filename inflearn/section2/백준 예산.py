N = int(input())
a = list(map(int, input().split()))
k = int(input())
lt = 0
rt = max(a)  # 150
mid = (lt+rt)//2  # 75
while lt <= rt:
    sum = 0
    for i in a:
        if i > mid:
            sum += mid
        else:
            sum += i
    if sum <= k:
        lt = mid+1
    else:
        rt = mid-1
    mid = (lt+rt)//2
print(mid)
