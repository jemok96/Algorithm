N = int(input())
a = [*map(int, input().split())]
M = int(input())

for i in range(M):
    max_index = a.index(max(a))
    min_index = a.index(min(a))
    a[max_index] -= 1
    a[min_index] += 1
    a.sort()
print(a[-1]-a[0])
