N, K = map(int, input().split())
a = list(map(int, input().split()))
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
    print(mid, check(mid))
    if check(mid) >= K:  # 자르고 남은 나무 길이의 합이 가져갈려는 길이보다 크기때문에  절단기에 설정할 수 있는 높이의 최댓값을 구해줌 => lt = mid +1
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
