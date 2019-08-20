import sys
sys.stdin = open('bj14503_로봇청소기.txt', 'r')

def IsSafe(y,x):
    return 0<=y<Y and 0<=x<X

def DFS(y, x, dir):
    if MyMap[y][x] == 0:
        MyMap[y][x] = 2

    dir_turn_left = dir
    for i in range(4):
        dir_turn_left = (dir_turn_left+3) % 4
        left_y = y + dy[dir_turn_left]
        left_x = x + dx[dir_turn_left]
        if IsSafe(left_y, left_x) and MyMap[left_y][left_x] == 0:
            DFS(left_y, left_x, dir_turn_left)
            return

    #후진 가능 여부
    dir_turn_back = (dir+2) % 4
    back_y = y + dy[dir_turn_back]
    back_x = x + dx[dir_turn_back]
    if IsSafe(back_y, back_x):
        if MyMap[back_y][back_x] != 1:
            DFS(back_y, back_x, dir)
        if MyMap[back_y][back_x]:
            return

Y, X = map(int, input().split())
start_y, start_x, start_dir = map(int, input().split())
MyMap = [list(map(int, input().split())) for _ in range(Y)]

#상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

DFS(start_y, start_x, start_dir)

ans = 0
for y in range(Y):
    for x in range(X):
        if MyMap[y][x] == 2:
            ans += 1

print(ans)

