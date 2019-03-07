import sys
sys.stdin = open('4875_미로_BFS.txt', 'r')

def IsSafe(y,x):
    return 0<=y<N and 0<=x<N and (Maze[y][x] == 0 or Maze[y][x] == 3)

def BFS(y, x):
    global result
    Q.append([y, x])
    visited.append((y, x))
    distance[y][x] = 0

    while Q:
        y, x = Q.pop(0)
        for dir in range(4):
            NewY = y + dy[dir]
            NewX = x + dx[dir]
            if IsSafe(NewY, NewX) and (NewY, NewX) not in visited:
                visited.append((NewY, NewX))
                Q.append((NewY, NewX))
                distance[NewY][NewX] = distance[y][x] + 1
                if Maze[NewY][NewX] == 3:
                    result = 1
                    return




TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]
    distance = [[0]*N for _ in range(N)]

    #상 하 좌 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for y in range(N):
        for x in range(N):
            if Maze[y][x] == 2:
                start_y, start_x = y, x

    visited = []
    result = 0
    Q = []
    BFS(start_y, start_x)
    print(result)
    print(distance)




