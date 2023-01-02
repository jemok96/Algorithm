N, S = map(int, input().split())
a = list(map(int, input().split()))
distance = []


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


ans = abs(S-a[0])
if S == 1:
    print(ans)
else:
    for x in a:
        distance.append(abs(x-S))
    mx = gcd(distance[0], distance[1])
    for i in range(len(distance)-1):
        num = gcd(mx, gcd(distance[i], distance[i+1]))
        if num > mx:
            mx = num
    print(mx)
