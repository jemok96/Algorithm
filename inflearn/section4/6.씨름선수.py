N = int(input())

lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))
lst.sort(reverse=True)
max = 0
cnt = 0
for s, e in lst:
    if e >= max:
        max = e
        cnt += 1
print(cnt)
