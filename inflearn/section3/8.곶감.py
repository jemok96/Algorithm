N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

T = int(input())
sum = 0

for _ in range(T):
    s, e, k = map(int, input().split())
    if e == 0:
        for i in range(k):
            lst[s-1].append(lst[s-1].pop(0))
    else:
        for i in range(k):
            lst[s-1].insert(0, lst[s-1].pop())

s = 0
e = N
for i in range(N):
    for j in range(s, e):
        sum += lst[i][j]
    if i < N//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(sum)
