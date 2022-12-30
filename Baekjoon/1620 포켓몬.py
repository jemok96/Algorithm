import sys
input = sys.stdin.readline
N, M = map(int, input().split())
names = dict()
for i in range(1, N+1):
    name = input().rstrip()
    names[i] = name
    names[name] = i


for _ in range(M):
    s = input().rstrip()
    if s.isdigit():
        print(names[int(s)])
    else:
        print(names[s])
