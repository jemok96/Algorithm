N = int(input())
lst = []
for _ in range(N):
    a = list(map(int, input().split()))
    lst.append(a)
sum = 0
s = N//2
e = s+1

for i in range(N):
    for j in range(s, e):
        sum += lst[i][j]
    if i < N//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(sum)
