N, K = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
print(a[K-1])
