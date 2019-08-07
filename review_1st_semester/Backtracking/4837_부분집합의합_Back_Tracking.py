import sys

sys.stdin = open("4837_부분집합의합.txt", "r")

def DFS(x):
    global final_result

    if len(result) == N and sum(result) == K:
        final_result += 1
        return

    if len(result) > N or sum(result) > K:
        return

    for i in range(len(Data)):
        if not visited[i]:
            if not result:
                visited[i] = 1
                result.append(Data[i])
                DFS(x+1)
                visited[i] = 0
                result.remove(Data[i])
            if result and Data[i] > result[-1]:
                visited[i] = 1
                result.append(Data[i])
                DFS(x+1)
                visited[i] = 0
                result.remove(Data[i])


TC = int(input())

for tc in range(1, TC+1):
    N, K = map(int, input().split())
    Data = [x for x in range(1,13)]
    visited = [0]*12
    final_result = 0
    result = []
    DFS(0)
    print('#%d %d'%(tc, final_result))

