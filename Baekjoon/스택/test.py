def min(a, b):
    while b > 0:
        a, b = b, a % b
    return a


a, b = map(int, input().split())
print(min(a, b))
print(int(a*b/min(a, b)))
