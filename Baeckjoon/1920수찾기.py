N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

a.sort()


def check(x):
    lt = 0
    rt = N-1
    while lt <= rt:
        mid = (lt + rt)//2

        if a[mid] == x:
            return True
        elif a[mid] < x:
            lt = mid + 1
        else:
            rt = mid - 1
    return False


for x in b:
    if check(x):
        print(1)
    else:
        print(0)
