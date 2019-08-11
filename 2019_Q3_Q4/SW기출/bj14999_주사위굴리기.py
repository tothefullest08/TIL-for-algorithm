import sys
sys.stdin = open('bj14999_주사위굴리기.txt', 'r')

def up():
    tmp_map[0][1] = dice_map[1][1]  # 뒤 <= 위
    tmp_map[1][1] = dice_map[2][1]  # 위 <= 앞
    tmp_map[2][1] = dice_map[3][1]  # 앞 <= 아래
    tmp_map[3][1] = dice_map[0][1]  # 아래 <= 뒤

    tmp_map[1][0] = dice_map[1][0]
    tmp_map[1][2] = dice_map[1][2]

    for y in range(4): dice_map[y][:] = tmp_map[y][:]

def down():
    tmp_map[0][1] = dice_map[3][1]  # 뒤 <= 아래
    tmp_map[1][1] = dice_map[0][1]  # 위 <= 뒤
    tmp_map[2][1] = dice_map[1][1]  # 앞 <= 위
    tmp_map[3][1] = dice_map[2][1]  # 아래 <= 앞

    tmp_map[1][0] = dice_map[1][0]
    tmp_map[1][2] = dice_map[1][2]

    for y in range(4): dice_map[y][:] = tmp_map[y][:]

def right():
    tmp_map[1][0] = dice_map[3][1]  # 서 <= 아래
    tmp_map[1][1] = dice_map[1][0]  # 위 <= 서
    tmp_map[1][2] = dice_map[1][1]  # 동 <= 위
    tmp_map[3][1] = dice_map[1][2]  # 아래 <= 동

    tmp_map[0][1] = dice_map[0][1]
    tmp_map[2][1] = dice_map[2][1]

    for y in range(4): dice_map[y][:] = tmp_map[y][:]

def left():
    tmp_map[1][0] = dice_map[1][1]  # 서 <= 위
    tmp_map[1][1] = dice_map[1][2]  # 위 <= 동
    tmp_map[1][2] = dice_map[3][1]  # 동 <= 아래
    tmp_map[3][1] = dice_map[1][0]  # 아래 <= 서

    tmp_map[0][1] = dice_map[0][1]
    tmp_map[2][1] = dice_map[2][1]

    for y in range(4): dice_map[y][:] = tmp_map[y][:]

def IsSafe(y,x):
    return 0<=y<Y and 0<=x<X


Y, X, start_y, start_x, turn = map(int, input().split())
MyMap = [list(map(int, input().split())) for _ in range(Y)]
order = list(map(int, input().split()))

# print(MyMap)
# print(order)

#공백 / 우 좌 상 하
dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]
dice_map = [[0]*3 for _ in range(4)]

for dir in order:
    # print(dir)
    n_y = start_y + dy[dir]
    n_x = start_x + dx[dir]
    tmp_map = [[0] * 3 for _ in range(4)]

    if IsSafe(n_y, n_x):
        if dir == 1: right()
        if dir == 2: left()
        if dir == 3: up()
        if dir == 4: down()

        # if dice_map[3][1] == 0:
        #     dice_map[3][1] = MyMap[n_y][n_x] 시발롬아

        if MyMap[n_y][n_x] == 0:
            MyMap[n_y][n_x] = dice_map[3][1]

        else:
            dice_map[3][1] = MyMap[n_y][n_x]
            MyMap[n_y][n_x] = 0

        start_y, start_x = n_y, n_x

        print(dice_map[1][1])











