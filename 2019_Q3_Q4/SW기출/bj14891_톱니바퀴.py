import sys
sys.stdin = open('bj14891_톱니바퀴.txt','r')

# 톱니바퀴는 총 4개
# K번 회전 시킴 // 시계방향 & 반시계방향으로 나뉨
# 방향과 회전시킬 톱니바퀴 결정
# 맞닿는 극이 다르면 돌린 방향과 반댓방향으로 회전시킴

def change_dir(y, dir):
    tmp = [0]*8
    if dir == 1: #시계방향
        tmp[0] = gear[y][7]
        tmp[1] = gear[y][0]
        tmp[2] = gear[y][1]
        tmp[3] = gear[y][2]
        tmp[4] = gear[y][3]
        tmp[5] = gear[y][4]
        tmp[6] = gear[y][5]
        tmp[7] = gear[y][6]

    elif dir == -1: #시계반대방향
        tmp[0] = gear[y][1]
        tmp[1] = gear[y][2]
        tmp[2] = gear[y][3]
        tmp[3] = gear[y][4]
        tmp[4] = gear[y][5]
        tmp[5] = gear[y][6]
        tmp[6] = gear[y][7]
        tmp[7] = gear[y][0]

    gear[y][:] = tmp
    return

gear = [list(map(int, input())) for _ in range(4)]

K = int(input())

for i in range(K):
    selected_y, direction = map(int, input().split())
    selected_y -= 1
    inspection_lst = [0]*4
    direction_lst = [0]*4

    #톱니바퀴 도는지 검증
    if selected_y == 0:
        inspection_lst[0] = 1
        if gear[0][2] != gear[1][6]: inspection_lst[1] = 1
        if inspection_lst[1] == 1 and gear[1][2] != gear[2][6]: inspection_lst[2] = 1
        if inspection_lst[2] == 1 and gear[2][2] != gear[3][6]: inspection_lst[3] = 1

        for j in range(4):
            if inspection_lst[j] == 1:
                if j % 2 == 0: direction_lst[j] = direction
                else: direction_lst[j] = direction * -1

    elif selected_y == 1:
        inspection_lst[1] = 1
        if gear[0][2] != gear[1][6]: inspection_lst[0] = 1
        if gear[1][2] != gear[2][6]: inspection_lst[2] = 1
        if inspection_lst[2] == 1 and gear[2][2] != gear[3][6]: inspection_lst[3] = 1

        for j in range(4):
            if inspection_lst[j] == 1:
                if j % 2 == 1: direction_lst[j] = direction
                else: direction_lst[j] = direction * -1

    elif selected_y == 2:
        inspection_lst[2] = 1
        if gear[2][2] != gear[3][6]: inspection_lst[3] = 1
        if gear[1][2] != gear[2][6]: inspection_lst[1] = 1
        if inspection_lst[1] == 1 and gear[0][2] != gear[1][6]: inspection_lst[0] = 1

        for j in range(4):
            if inspection_lst[j] == 1:
                if j % 2 == 0: direction_lst[j] = direction
                else: direction_lst[j] = direction * -1

    elif selected_y == 3:
        inspection_lst[3] = 1
        if gear[2][2] != gear[3][6]: inspection_lst[2] = 1
        if inspection_lst[2] == 1 and gear[1][2] != gear[2][6]: inspection_lst[1] = 1
        if inspection_lst[1] == 1 and gear[0][2] != gear[1][6]: inspection_lst[0] = 1

        for j in range(4):
            if inspection_lst[j] == 1:
                if j % 2 == 1: direction_lst[j] = direction
                else: direction_lst[j] = direction * -1

    #톱나바퀴 돌리기
    for k in range(4):
        if direction_lst[k] != 0:
            change_dir(k, direction_lst[k])
    # print(gear)

# print(gear)
ans = 0
for y in range(4):
    if gear[y][0] == 1:
        ans += 2**y

print(ans)





#돌리기 전, 맞닿는 위치 극 확인
#다를 경우, 돌릴 준비
#그 옆에 있는 경우도 확인해야함

#첫번째 톱니바퀴가 선정된 경우
#1번 바퀴의 2번방과 2번바퀴의 6번방 비교 => 서로 다른 경

