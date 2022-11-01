N = int(input())
lst = list(map(int, input().split()))


def check(num):
    sum = 0
    while(num > 0):
        sum += num % 10
        num //= 10
    # for i in num:
    #   sum+=int(i)
    return sum


min = 0
result = lst[0]
for i in lst:
    x = check(i)
    if(x > min):
        min = x
        lst = i
print(lst)
