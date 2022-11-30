N, M = map(int, input().split())
a = []
check = set()
for _ in range(N):
    a.append(input())
for _ in range(M):
    check.add(input())

cnt = 0
for i in check:
    if i in a:
        cnt += 1
print(cnt)
