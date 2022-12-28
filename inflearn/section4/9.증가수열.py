n = int(input())
a = list(map(int, input().split()))
lt = 0
rt = n-1
last = 0
stack = []
res = ''

while lt <= rt:
