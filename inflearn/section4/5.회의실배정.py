N = int(input())
lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))
lst.sort(key=lambda x: (x[1], x[0]))

cnt = 1

s = lst[0][0]
e = lst[0][1]

for x in range(1, N):
    if (e <= lst[x][0]):
        e = lst[x][1]

        cnt += 1

print(cnt)
