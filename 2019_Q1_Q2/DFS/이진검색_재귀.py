# 2 4 7 9 11 19 23


Data = [2, 4, 7, 9, 11, 19, 23]
N = len(Data)
start = 0
end = N - 1

def DFS(x):
    global start, end, result

    if start == end:
        return

    mid = (start + end) // 2

    if Data[mid] < x:
        start = mid +1

    elif Data[mid] > x:
        end = mid -1
    else:
        result = mid
        return

    DFS(x)

result = -1
DFS(9)
print(result)
