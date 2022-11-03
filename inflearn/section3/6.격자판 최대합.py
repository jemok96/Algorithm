N = int(input())
lst = []
for _ in range(N):
    a = list(map(int, input().split()))
    lst.append(a)


max = 0
for i in range(N):
    row = 0
    col = 0
    for j in range(N):
        row += lst[i][j]
        col += lst[j][i]
    if row > max:
        max = row
    if col > max:
        max = col

dia = 0
dia2 = 0
for i in range(N):
    dia += lst[i][i]
    dia2 += lst[i][N-j-1]
if dia > max:
    max = dia
if dia2 > max:
    max = dia2
print(max)
