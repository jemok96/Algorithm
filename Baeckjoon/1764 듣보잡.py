N, M = map(int, input().split())
a = set()
b = set()
for _ in range(N):
    a.add(input())
for _ in range(M):
    b.add(input())

result = a.intersection(b)
result = list(result)
result.sort()
print(len(result))
for x in result:
    print(x)
