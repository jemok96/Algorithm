N = int(input())
a = list(map(int, input().split()))
result = 0
cnt = 0
for i in a:
    if(i == 1):
        cnt += 1
        result += cnt
    else:
        cnt = 0
print(result)
