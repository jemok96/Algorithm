# paper = [[0 for _ in range(100)] for _ in range(100)]


# for i in range(100):
#     for j in range(100):
#         paper[i][j] = 1

# N = int(input())
# for _ in range(N):
#     a, b = map(int, input().split())
#     paper[100-b][100-a] = 0

# for i in paper:
#     for j in i:
#         print(j, end=' ')
#     print()
paper = [[0 for _ in range(10)] for _ in range(10)]


for i in range(10):
    for j in range(10):
        paper[i][j] = 1

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    paper[10-b][a-1] = 0

for i in paper:
    for j in i:
        print(j, end=' ')
    print()
