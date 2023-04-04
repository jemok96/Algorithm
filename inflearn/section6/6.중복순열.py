import sys
input = sys.stdin.readline


def DFS(L):
    global cnt
    if L == m:
        for i in range(m):
            print(ch[i], end=" ")
        print()
        cnt += 1

    else:
        for i in range(1, n+1):
            ch[L] = i
            DFS(L+1)


n, m = map(int, input().split())
ch = [0]*m
cnt = 0
DFS(0)
print(cnt)
