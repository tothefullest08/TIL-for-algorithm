import sys

sys.stdin = open('4881_최소합.txt', 'r')

def DFS(y):
    global result, final_result

    if final_result < result:
        return


    if y == N:
        if result < final_result:
            final_result = result
            return

    for x in range(N):
        if not visited[x]:
            visited[x] = 1
            result += Data[y][x]
            DFS(y+1)
            visited[x] = 0
            result -= Data[y][x]



TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 0
    final_result = 987654321
    DFS(0)
    print('#%d %d'%(tc, final_result))
