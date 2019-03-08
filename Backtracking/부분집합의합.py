
def DFS(x):
    if len(result) == 3:
        print(result)
        return
    for i in range(N):
        if Data[i] not in visited:
            if not visited:
                visited.append(Data[i])
                result.append(Data[i])
                DFS(x+1)
                visited.remove(Data[i])
                result.remove(Data[i])
            elif visited and Data[i] > visited[-1]:
                visited.append(Data[i])
                result.append(Data[i])
                DFS(x+1)
                visited.remove(Data[i])
                result.remove(Data[i])


Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(Data)
visited = [0] * N
result = []
DFS(0)
