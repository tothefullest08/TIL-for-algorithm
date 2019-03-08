

Data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
v = max(Data)
e = len(Data)//2
MyMap = [[0]*(v+1) for i in range(v+1)]

def BFS(start):
    visited[start] = 1
    Q.append(start)

    while Q:
        start = Q.pop(0)
        print(start)
        for next in range(1, v+1):
            if MyMap[start][next] and not visited[next]:
                Q.append(next)
                visited[next] = 1



for i in range(e):
    start = Data[i*2]
    stop = Data[i*2+1]
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1

visited = [0]*(v+1)
Q = []
distance = 0
BFS(1)

print(MyMap)