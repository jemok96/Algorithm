# nCr 일 때  n!/ (n-r)! * r!
# (n-r)! 와 r!의  2,5의 개수를 구해서 더 작은 값이 0의개수
# 5의 지수 => n! 5의지수에서 r! - (n-r)!
N, M = map(int, input().split())


def count_number(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt


five = count_number(N, 5) - count_number(M, 5) - count_number(N-M, 5)
two = count_number(N, 2) - count_number(M, 2) - count_number(N-M, 2)
print(min(five, two))
