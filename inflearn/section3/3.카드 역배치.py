lst = list(range(21))
# print(lst)

for i in range(10):
    s, e = map(int, input().split())
    size = (e-s+1)//2
    for j in range(size):
        lst[s+j], lst[e-j] = lst[e-j], lst[s+j]
for i in range(1, len(lst)):
    print(lst[i], end=' ')
