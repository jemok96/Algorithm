a, b = 120, 48
# 최대공약수

#GCD : 최대공약수


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


print(a)

# 최소공배수


def lcm(a, b):
    return int(a*b/gcd(a, b))


print(lcm(a, b))
