a = []
for i in range(9):
    x = list(map(int, input().split()))
    a.append(x)
max = 0
row = 0
col = 0
for i in range(9):
    for j in range(9):
        if(a[i][j] > max):
            max = a[i][j]
            row = i+1
            col = j+1
print(max)
print(row, col)
