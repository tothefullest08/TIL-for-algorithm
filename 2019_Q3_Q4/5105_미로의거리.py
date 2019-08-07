import sys
sys.stdin = open('5105_미로의거리.txt', 'r')

def IsSafe(y,x):
    return 0<= y < N and 0<= x < N and (Maze[y][x] == 0 or Maze[y][x] == 3)


def BFS():
    global final_y, final_x, result

    while Q:
        y, x = Q.pop(0)
        visited[y][x] = 1

        if Maze[y][x] == 3:
            final_y, final_x = y, x
            result = distance[y][x] - 1
            break

        for dir in range(4):
            new_y = y + dy[dir]
            new_x = x + dx[dir]
            if IsSafe(new_y, new_x) and not visited[new_y][new_x]:
                Q.append([new_y, new_x])
                distance[new_y][new_x] = distance[y][x] + 1


TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]

    start_y, start_x = 0, 0
    for y in range(N):
        for x in range(N):
            if Maze[y][x] == 2:
                start_y, start_x = y, x

    visited = [[0]*N for _ in range(N)]
    distance = [[0]*N for _ in range(N)]

    #상 하 좌 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]


    Q = [[start_y, start_x]]

    final_y, final_x = 0, 0
    result = 0
    BFS()

    print('#%d %d'%(tc, result))


