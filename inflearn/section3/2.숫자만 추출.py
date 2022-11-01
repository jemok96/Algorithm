s = input()

result = 0
cnt = 0
for x in s:
    if x.isdecimal():
        result = result * 10 + int(x)
for i in range(1, result+1):
    if result % i == 0:
        cnt += 1
print(result)
print(cnt)
