def MyCalc(start):
    global result, final_result
    if sum(result) == 10:
        final_result.append(result.copy())
        return

    if sum(result) > 10:
        return

    for i in range(N):
        if not visited[i]:
            if not result:
                visited[i] = True
                result.append(Data[i])
                MyCalc(start+1)
                visited[i] = False
                result.remove(Data[i])

            if result and Data[i] > result[-1]:
                visited[i] = True
                result.append(Data[i])
                MyCalc(start+1)
                visited[i] = False
                result.remove(Data[i])

Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(Data)
visited = [0]*N
result, final_result = [], []
MyCalc(0)
print(final_result)