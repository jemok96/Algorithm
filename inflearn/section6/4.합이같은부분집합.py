import sys


def DFS(L, sum):
    # sum 내가만든 부분집합 합
    if sum > total//2:
        return
    if L == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)


n = int(input())
a = list(map(int, input().split()))
total = sum(a)  # 전체합

DFS(0, 0)
print("NO")
