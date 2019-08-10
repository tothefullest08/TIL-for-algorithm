import sys
sys.stdin = open('bj17143_낚시왕.txt', 'r')

def isSafe(y,x):
    return 0<=y<Y and 0<=x<X

def move(y,x, life, dir, size):

    if life == 0:
        if new_map[y][x] > size:
            return
        new_map[y][x] = size
        shark_info[size][1] = dir
        return

    n_y = y + dy[dir]
    n_x = x + dx[dir]
    if isSafe(n_y, n_x):
        move(n_y, n_x, life-1, dir, size)

    #상어 방향 전환 case
    else:
        if dir == 0: dir = 1
        elif dir == 1: dir = 0
        elif dir == 2: dir = 3
        elif dir == 3: dir = 2
        n_y = y + dy[dir]
        n_x = x + dx[dir]
        if isSafe(n_y, n_x):
            move(n_y, n_x, life-1, dir, size)


Y, X, M = map(int, input().split())
my_map = [[0] * X for _ in range(Y)]
shark_info = {}
for i in range(M):
    y, x, speed, direction, z = map(int, input().split())
    shark_info[z] = [speed,  direction- 1]
    my_map[y-1][x-1] = z

# 상, 하, 우, 좌
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

ans = 0
# 턴 이동
for turn in range(X):

    # 상어 사냥
    for y in range(Y):
        if my_map[y][turn]:
            ans += my_map[y][turn]
            del shark_info[my_map[y][turn]]  # 상어 정보 삭제
            my_map[y][turn] = 0  # 상어 제거
            break

    # 새로운 배열 생성
    new_map = [[0]*X for _ in range(Y)]

    #상어 이동
    for y in range(Y):
        for x in range(X):
            if my_map[y][x]:
                size = my_map[y][x]
                life = shark_info[size][0]
                dir = shark_info[size][1]
                move(y, x, life, dir, size)
    # print(new_map)

    #새로운 상어 위치 기반으로 맵 변경
    for y in range(Y):
        my_map[y][:] = new_map[y][:]

print(ans)