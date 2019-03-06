import sys
sys.stdin = open('1210_ladder.txt', 'r')

def IsSafe(y, x):
    return 0<=y<100 and 0<=x<100 and Ladder[y][x] == 1


def DFS(y, x):
    global result
    visited.append((y, x))

    if y == 0:
        result = x
        return

    for dir in range(3):
        NewY = y+dy[dir]
        NewX = x+dx[dir]
        if IsSafe(NewY, NewX) and not (NewY, NewX) in visited:
            break

    DFS(NewY, NewX)


for tc in range(1, 11):
    tc = int(input())
    Ladder = [list(map(int, input().split())) for _ in range(100)]

    start_y = 99
    start_x = Ladder[99].index(2)

    dy = [0, 0, -1]
    dx = [-1, 1, 0]

    result = 0
    visited = []
    DFS(start_y, start_x)
    print('#%d %d'%(tc, result))






