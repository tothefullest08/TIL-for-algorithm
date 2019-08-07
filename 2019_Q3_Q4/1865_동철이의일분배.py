import sys
sys.stdin = open('1865_동철이의일분배.txt', 'r')

def DFS(y):
    global result, sub_result

    if sub_result <= result:
        return

    if y == N:
        result = sub_result
        return

    for x in range(N):
        if not visited[x]:
            if MyMap[y][x] == 0:
                continue
            else:
                visited[x] = 1
                sub_result *= (MyMap[y][x] / 100)
                DFS(y+1)
                visited[x] = 0
                sub_result /= (MyMap[y][x]/100)

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    MyMap = [list(map(int, input().split())) for _ in range(N)]
    # print(MyMap)

    visited = [0] * N
    result, sub_result = 0, 1
    DFS(0)
    print('#%d %0.6f'%(tc, round(result*100, 6)))