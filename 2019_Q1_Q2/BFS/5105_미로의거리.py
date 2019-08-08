import sys
sys.stdin = open('5105_미로의거리.txt', 'r')

def IsSafe(y, x):
    return 0<=y<N and 0<=x<N and (Miro[y][x]==0 or Miro[y][x]==3)

def BFS(y, x):
    global result
    Q.append((y,x))
    visited.append((y,x))

    while Q:
        y, x = Q.pop(0)
        for dir in range(4):
            y1 = y + dy[dir]
            x1 = x + dx[dir]
            if IsSafe(y1, x1) and (y1, x1) not in visited:
                Q.append((y1,x1))
                visited.append((y1,x1))
                distance[y1][x1] = distance[y][x] +1
                if Miro[y1][x1] == 3:
                    result = distance[y1][x1]-1
                    return


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Miro = [list(map(int, input())) for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if Miro[y][x] == 2:
                start_y, start_x = y, x

    dy = [-1, 1, 0 ,0]
    dx = [0, 0, -1, 1]

    Q = []
    visited = []
    distance = [[0]*N for _ in range(N)]
    result = 0

    BFS(start_y, start_x)
    print('#%d %d'%(tc, result))
