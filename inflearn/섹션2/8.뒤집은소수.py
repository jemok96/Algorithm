N = int(input())
a = list(map(int, input().split()))


def reverse(x):

    result = 0
    while(x > 0):
        tmp = x % 10
        result = 10*result + tmp
        x //= 10
    return result


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):  # 절반까지 나눠떨어지는게 있으면 소수가 아님
        if x % i == 0:
            return False
    return True


for x in a:
    reverseX = reverse(x)
    if(isPrime(reverseX)):
        print(reverseX, end=' ')
