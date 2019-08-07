import sys
sys.stdin = open("연습문제3_달팽이.txt", "r")

Init_Data = [list(map(int, input().split())) for _ in range(5)]

Amended_Data = []
for y in range(5):
    for x in range(5):
        Amended_Data.append(Init_Data[y][x])
Amended_Data.sort()


Maze = [[0]*5 for _ in range(5)]

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def IsSafe(y,x):
    return 0 <= y < 5 and 0 <= x < 5 and Maze[y][x] == 0


start_x, start_y = 0, 0
for i in range(len(Amended_Data)):
    Maze[start_y][start_x] = Amended_Data[i]
    for dir in range(4):
        if IsSafe(start_y + dy[dir], start_x + dx[dir]):
            start_y += dy[dir]
            start_x += dx[dir]
            break


print(Maze)




