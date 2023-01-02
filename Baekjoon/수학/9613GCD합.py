n = int(input())


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


for _ in range(n):
    a = list(map(int, input().split()))
    sum = 0
    for i in range(1, len(a)-1):
        for j in range(i+1, len(a)):
            sum += gcd(a[i], a[j])
            # print("a[i] = {} a[j]={}".format(a[i], a[j]))
            # print(sum)
    print(sum)
