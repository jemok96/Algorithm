
def DFS(L, sum, tsum):
    global result
    if (total - tsum) + sum < result:
        return
    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum)

    return sum


c, n = map(int, input().split())
a = [0]*n
result = -214700000
for i in range(n):
    a[i] = int(input())
total = sum(a)
DFS(0, 0, 0)
print(result)
