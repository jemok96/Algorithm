# 투 포인터
N = int(input())
a = list(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

res = []
p1 = 0
p2 = 0
size = min(N, M)
print(size)

while (p1 < N and p2 < M):
    if a[p1] <= b[p2]:
        res.append(a[p1])
        p1 += 1
    else:
        res.append(b[p2])
        p2 += 1
if M > p2:
    res += b[p2:]
elif N > p1:
    res += a[p1:]

print(p1, p2)
print(res)
