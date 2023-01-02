n = int(input())
# n <=500일 때  n! 0의 개수는 소인수분해 했을 때 0의 개수임
# 25는 5^2(2개)  125는 5^3(3개)
cnt = 0
cnt += n//5
cnt += n//25
cnt += n//125
print(cnt)
