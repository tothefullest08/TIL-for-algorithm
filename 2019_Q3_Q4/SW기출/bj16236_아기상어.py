import sys
sys.stdin = open('bj16236_아기상어.txt', 'r')

def IsSafe(y,x):
    return 0<=y<N and 0<=x<N

def BFS(init_y, init_x):
    while Q:
        y, x = Q.pop(0)

        #물고기 리스트에 무언가가 들어있는 경우,
        if fish_lst:
            if distance[y][x] == fish_lst[0][2] and 0< MyMap[y][x] < shark_info[9][2] and [y,x, distance[y][x]] not in fish_lst:
                fish_lst.append([y,x, distance[y][x]])
                continue
            elif distance[y][x] > fish_lst[0][2]:
                continue

        for dir in range(4):
            n_y = y + dy[dir]
            n_x = x + dx[dir]
            #테두리 안 조건, visited 조건, 처음위치 방문x 조건, 상어보다 같거나 작은 위치로 이동가능 조건
            if IsSafe(n_y, n_x) and distance[n_y][n_x] == 0 and (n_y, n_x) != (init_y, init_x) and 0 <= MyMap[n_y][n_x] <= shark_info[9][2]:
                # 물고기 리스트가 비어있고, 상어보다 작은 물고기를 찾은 경우: 물고기 리스트에 추가
                if not fish_lst and 1 <= MyMap[n_y][n_x] < shark_info[9][2]:
                    distance[n_y][n_x] = distance[y][x] + 1
                    fish_lst.append([n_y, n_x, distance[n_y][n_x]])
                    continue

                Q.append([n_y, n_x])
                distance[n_y][n_x] = distance[y][x] + 1

N = int(input())
MyMap = [list(map(int, input().split())) for _ in range(N)]

shark_info = {}
for y in range(N):
    for x in range(N):
        if MyMap[y][x] == 9:
            shark_info[9] = [y,x,2]

fish_ate, time_passed = 0, 0

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 잡아먹을 물고기 위치 찾기
while True:
    distance = [[0]*N for _ in range(N)]
    Q = []
    fish_lst = []
    Q. append([shark_info[9][0], shark_info[9][1]])
    BFS(shark_info[9][0], shark_info[9][1])
    # print(fish_lst)

    #반복문 종료 조건: 더이상 상어가 물고기를 먹을수 없는 경우
    if not fish_lst:
        break

    #기존의 상어위치를 0으로 변경
    MyMap[shark_info[9][0]][shark_info[9][1]] = 0

    # 잡아먹을 물고기 최종 선정
    if len(fish_lst) == 1:
        shark_info[9][0] = fish_lst[0][0]
        shark_info[9][1] = fish_lst[0][1]

    else:
        fish_lst.sort(key=lambda x:x[0])
        fish_y, fish_x = fish_lst[0][0], fish_lst[0][1]
        for i in range(1, len(fish_lst)):
            if fish_lst[i][0] > fish_y:
                break
            elif fish_lst[i][0] == fish_y and fish_lst[i][1] < fish_x:
                fish_y = fish_lst[i][0]
                fish_x = fish_lst[i][1]

        shark_info[9][0] = fish_y
        shark_info[9][1] = fish_x

    #물고기 먹은 횟수 & 시간 변경
    fish_ate += 1
    time_passed += fish_lst[0][2]

    #물고기 먹은 위치로 상어 이동
    MyMap[shark_info[9][0]][shark_info[9][1]] = 9

    #상어 크기 변경
    if fish_ate == shark_info[9][2]:
        shark_info[9][2] += 1
        fish_ate = 0

print(time_passed)




#탐색
#물고기<상어 위치(+거리)를 찾음
#첫번째 물고기를 찾아서, 그 거리를 기준으로 거리까지 물고기가 있는지를 검색
#더이상 없으면 종료
#같은 거리의 물고기가 여러개일 경우 1. y값이 작은 것을 찾음. 2. 동일한 y값인 경우, x갑이 작은 것을 찾음
#물고기 먹은 횟수 카운팅
#움직인 시간 카운팅
#더이상 움직일 곳이 없으면 종료

