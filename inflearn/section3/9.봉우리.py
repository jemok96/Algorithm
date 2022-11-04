N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

a.insert(0, [0]*N)
a.append([0]*N)

for i in range(len(a)):
    a[i].append(0)
    a[i].insert(0, 0)

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
for i in range(1, N+1):
    for j in range(1, N+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)
