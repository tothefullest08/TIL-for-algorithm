



def DFS(start):
    # print(start)
    visited[start] = 1
    for next in range(1, v+1):
        if MyMap[start][next] and not visited[next]:
            print(next)
            DFS(next)


Data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
e = len(Data)//2
v = max(Data)
visited = [0]*(v+1)
MyMap = [[0]*(v+1) for _ in range(v+1)]
result = []
for i in range(e):
    start = Data[i*2]
    end = Data[i*2+1]
    MyMap[start][end] = 1
    MyMap[end][start] = 1

DFS(1)
# print(result)