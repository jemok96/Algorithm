N, M = map(int, input().split())
names = dict()
for i in range(1, N+1):
    name = input().rstrip()
    names[i] = name
    names[name] = i


for _ in range(M):
    s = input()
    if s.isdigit():
        print(names[int(s)])
    else:
        print(names[s])
