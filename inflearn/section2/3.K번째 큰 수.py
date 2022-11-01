N, K = map(int, input().split())
a = list(map(int, input().split()))
lst = set()
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            lst.add(a[i]+a[j]+a[k])
lst = list(lst)
lst.sort(reverse=True)
print(lst[K-1])
