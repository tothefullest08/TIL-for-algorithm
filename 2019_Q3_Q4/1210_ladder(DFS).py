import sys
sys.stdin = open('1210_ladder.txt', 'r')

def IsSafe(y,x):
    return 0 <= y < 100 and 0<= x < 100 and MyMap[y][x] == 1

def DFS(y,x):
    global result
    visited[y][x] = 1
    if y == 0:
        result = x
        return

    for dir in range(3):
        new_y = y + dy[dir]
        new_x = x + dx[dir]
        if IsSafe(new_y, new_x) and not visited[new_y][new_x]:
            DFS(new_y, new_x)
            break


TC = 10
for tc in range(1, TC+1):
    N = int(input())
    MyMap = [list(map(int, input().split())) for _ in range(100)]
    # print(MyMap)

    start_y, start_x = 99, 0
    for x in range(100):
        if MyMap[99][x] == 2:
            start_x = x

    visited = [[0]*100 for _ in range(100)]

    #좌 우 상
    dy = [0, 0, -1]
    dx = [-1, 1, 0]

    result = 0

    DFS(start_y,start_x)
    print('#%d %d'%(tc, result))