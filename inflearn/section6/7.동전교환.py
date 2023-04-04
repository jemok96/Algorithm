import sys
input = sys.stdin.readline


def DFS(L, sum):
    global result
    if L > result:
        return
    if sum > m:
        return
    if sum == m:
        if L < result:
            result = L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])


n = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort(reverse=True)

result = 9999
DFS(0, 0)
print(result)
