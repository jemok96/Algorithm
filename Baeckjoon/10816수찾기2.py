N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

count = {}
for x in a:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

for x in b:
    res = count.get(x)
    if res == None:
        print(0, end=" ")
    else:
        print(res, end=" ")
