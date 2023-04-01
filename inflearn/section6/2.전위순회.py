# 전위순회 출력 : 1 2 4 5 3 6 7
# 중위순회 출력 : 4 2 5 1 6 3 7
# 후위순회 출력 : 4 5 2 6 7 3 1

def DFS(x):
    if x > 7:
        return
    else:
        print(x, end=" ")
        DFS(x*2)
        DFS(x*2+1)


DFS(1)
