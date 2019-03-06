import sys

sys.stdin = open("4837_부분집합의합.txt", "r")



def DFS(x):
    global result, final_result

    if sum(result) == K and len(result) == N:
        final_result.append(result.copy())
        return

    if sum(result) > K and len(result)> N:
        return

    for i in range(Len):
        if not visited[i]:
            visited[i] = 1
            result.append(num[i])
            DFS(x+1)
            visited[i] = 0
            result.remove(num[i])


TC  = int(input())
num = [1,2,3,4,5,6,7,8,9,10,11,12]
Len = len(num)


for tc in range(1, TC+1):
    N, K = map(int, input().split())
    visited = [0] * Len
    result, final_result = [], []
    DFS(0)

    print(final_result)

