n = int(input())
a = list(map(int, input().split()))
avg = round((sum(a)/n))  # round half_even방식 이라  avg = int(avg+0.5)
print(int(avg+0.5))
tmp = 9999999
score = 0
result = 0
for i in range(n):
    ab = abs(avg - a[i])
    if(tmp > ab):
        tmp = ab
        score = a[i]
        result = i
    if(tmp == ab):
        if(a[i] > score):
            score = a[i]
            result = i

print(avg, result+1)
