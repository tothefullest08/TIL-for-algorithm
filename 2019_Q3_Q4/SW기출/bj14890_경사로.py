import sys
sys.stdin = open('bj14890_경사로.txt','r')

#
# 크기 N * N 지도
# 각지도에는 높이가 명시
# 지나갈 수 있는 길 확인
#
# 길을 지나가려면 길에 속한 모든 칸의 높이가 같아야함.
# 경사로의 높이는 항상 1. 길이는 L개
# 경사로는 낮은칸과 높은 칸을 연결
#  - 낮은 칸에 설치. L개의 연속된칸에 경사로 바닥 모두 접해야함
#  - 낮은칸과 높은 칸의 차이는 1이어야함.
#  - 경사로를 놓은 낮은 칸의 높이는 모두 같아야하며, L개의 칸이 연속되어야함
#
# 경사로를 놓지 못하는 경우들
#  - 경사로를 놓은 곳에 또 놓는 경우
#  - 낮은 칸과 높은 칸의 차이가 1이 아닌 경우
#  - 낮으 지점의 칸의 높이가 모두 같지 않거나 L개가 연속되지 않은 경우
#  - 경사로를 놓다가 범위를 벗어나는 경우

#끝점만 보면됨. y축, x축
#1. 시작점부터 끝점까지 높이가 다 같은경우는 무조건 + 1
#2. 그렇지 않은경우
#2.1 시작점 다음 칸이 시작점칸 -1 또는 +1 인 경우 이동 가능
#2.2 경사로의 길이만큼 이동 (-1/+1)


def canGo1(y):
    global L, cnt

    visited = [0]*N
    visited[0] = 1
    start_height = MyMap[y][0]
    move = 0
    for x in range(1, N):
        current_height = MyMap[y][x]
        move += 1

        #높이가 같은 경우
        if start_height == current_height:
            visited[x] = 1
            continue

        #다음 칸이 더 높은 경우
        elif start_height + 1 == current_height:
            if move >= L:
                start_height = current_height
                move = 0
                visited[x] = 1
            else:
                break

        #다음 칸이 더 낮은 경우
        elif start_height -1 == current_height:
            if move >= L:
                start_height = current_height
                move = 0
                visited[x] = 1
            else:
                visited[x] = 1
    flag = 1
    for i in visited:
        if not i:
            flag = 0

    if flag:
        cnt += 1


def canGo2(x):
    global L, cnt

    visited = [0]*N
    visited[0] = 1
    start_height = MyMap[0][x]
    move = 0
    for y in range(1, N):
        current_height = MyMap[y][x]
        move += 1

        #높이가 같은 경우
        if start_height == current_height:
            visited[y] = 1
            continue

        #다음 칸이 더 높은 경우
        elif start_height + 1 == current_height:
            if move >= L:
                start_height = current_height
                move = 0
                visited[y] = 1
            else:
                break

        #다음 칸이 더 낮은 경우
        elif start_height -1 == current_height:
            if move >= L:
                start_height = current_height
                move = 0
                visited[y] = 1
            elif move < L:
                visited[y] = 1

    flag = 1
    for i in visited:
        if not i:
            flag = 0
            break

    if flag:
        cnt += 1



N, L = map(int, input().split())
MyMap = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for y in range(N):
    canGo1(y)

# for x in range(N):
#     canGo2(x)

print(cnt)



