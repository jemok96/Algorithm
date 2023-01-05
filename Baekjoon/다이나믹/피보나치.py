lst = [0]*46


def fibo(n):
    if n <= 1:
        return n
    else:
        if lst[n] > 0:
            return lst[n]
        lst[n] = fibo(n-1) + fibo(n-2)
        return lst[n]


n = int(input())
print(fibo(n))
print(cnt)
