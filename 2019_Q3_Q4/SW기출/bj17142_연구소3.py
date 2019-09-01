import sys
sys.stdin = open('bj17142_연구소3.txt','r')

import itertools

# 바이러스: 활성/비활성으로 나뉨
# 처음에는 모두 비활성. 활성으로 바뀔 경우 상/하/좌/우 바이러스 터짐
# 활성 바이러스가 비활성 바이러스로 갈 경우, 비활성 -> 활성으로 변경됨
# M개를 활성 상태로 변경하려고 함.
# 연구소의 크기는 N x N
# 0 - 빈칸 / 1 - 벽 / 2 - 바이러스


# 조합으로 M개 만큼 바이러스 활성 개수 지정
# BFS 로 돌림
# Distance 로 거리 계산

def IsSafe(y,x):
    return 0 <= y < N and 0 <= x < N

def BFS():
    global spreaded_so_far

    while Q:
        y, x = Q.pop(0)
        for dir in range(4):
            n_y = y + dy[dir]
            n_x = x + dx[dir]
            if IsSafe(n_y, n_x):
                if MyMap2[n_y][n_x] == -1: #비활성 바이러스를 활성으로 바꾸는 경우
                    MyMap2[n_y][n_x] = MyMap2[y][x] + 1
                    tmp.append([n_y, n_x]) #tmp 배열에 추가
                    Q.append([n_y, n_x])
                elif MyMap2[n_y][n_x] == 0 and [n_y, n_x] not in tmp:
                    MyMap2[n_y][n_x] = MyMap2[y][x] + 1
                    Q.append([n_y, n_x])
                    spreaded_so_far += 1


N, M = map(int, input().split())
MyMap = [list(map(int, input().split())) for _ in range(N)]

virus_lst = []
num_empty = 0
for y in range(N):
    for x in range(N):
        if MyMap[y][x] == 2: # 바이러스 위치는 -1으로 변경
            virus_lst.append([y,x])
            MyMap[y][x] = -1
        elif MyMap[y][x] == 1: # 벽은 -2로 재 저장
            MyMap[y][x] = -2
        elif MyMap[y][x] == 0: # 빈칸인 경우 빈칸 갯수 카운팅
            num_empty += 1

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

ans = 987654321
# 조합 계산
for combi in itertools.combinations(virus_lst, M):

    spreaded_so_far = 0
    Q = [] # Queue 선언

    # 지도 복사
    MyMap2 = [[0]*N for _ in range(N)]
    for y in range(N): MyMap2[y][:] = MyMap[y][:]

    tmp = []
    for i in combi:
        Q.append(i)
        tmp.append(i)
        MyMap2[i[0]][i[1]] = 0

    BFS()

    # 검증
    sub_ans = 0

    # 전부 퍼뜨리지 못한 경우 (지도에 바이러스 좌표를 제외한 빈칸이 있는 경우)
    if spreaded_so_far != num_empty:
        sub_ans = 987654311

    #퍼
    else:
        for y in range(N):
            for x in range(N):
                # tmp 배열에 있는 좌표에 저장된 거리 값은 포함 X
                if MyMap2[y][x] > sub_ans and [y,x] not in tmp:
                    sub_ans = MyMap2[y][x]

    if sub_ans < ans:
        ans = sub_ans

if ans == 987654311:
    print(-1)
else: print(ans)




