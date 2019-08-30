import sys
sys.stdin = open('bj16234_인구이동.txt', 'r')

# 땅 크기 - N x N
# 각 땅에는 나라가 존재, Map[y][x] 명이 살고 있음.
# 인구이동은 이동이 없을 때 까지 지속 => while문 사용하자
# 국경선 인구차이가 L명 이상 / R명 이하인경우 국경선 엶
# 조건에따라 국겨선이 모두 열리면 인구이동 시작
# 인접한 칸으로만 이동가능, 하루동안 연합이라 일컫음
# 연합내 각 칸의 인구수는 연합 인구수 / 칸의 개수 (소수점은 버림)
# 연합 해제후 국경선을 닫음.
# 각 나라의 인구수가 주어졌을 때, 인구이동 몇번하는지?

#종료 조건
def Check():
    global N
    for y in range(N):
        for x in range(N):
            # visited 배열에 -1이 아닌 값이 있는경우는 False 반환
            if visited[y][x] != -1: return False
    #visited 배열이 전부 -1인경우, True 반환
    return True

def IsSafe(y,x):
    return 0<=y<N and 0<=x<N


def BFS(init_y, init_x):
    global L, R

    Q = []
    #연합을 넣을 배열 선언
    union_sub_lst = []
    visited[init_y][init_x] = 1
    Q.append([init_y, init_x])
    union_sub_lst.append([init_y, init_x])

    while Q:
        y, x = Q.pop(0)
        for dir in range(4):
            n_y = y + dy[dir]
            n_x = x + dx[dir]
            #맵을 벗어나지않고, 연합 조건을 만족시키며, 방문하지 않은 칸인 경우
            if IsSafe(n_y, n_x) and L <= abs(MyMap[y][x] - MyMap[n_y][n_x]) <= R and visited[n_y][n_x] <= 0:
                visited[n_y][n_x] = 1
                Q.append([n_y, n_x]) #Queue에 append
                union_sub_lst.append([n_y, n_x]) #연합 배열에 추가

    # 연합 배열의 길이가 1 => 어디로도 이동하지 못한 경우
    if len(union_sub_lst) == 1:
        visited[init_y][init_x] = -1 #visited를 -1으로 선언
        return
    #그렇지 않은 경우는 전체 연합 배열에 현재의 연합배열을 append
    union_lst.append(union_sub_lst)


N, L, R = map(int, input().split())
MyMap = [list(map(int, input().split())) for _ in range(N)]

#상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


cnt = 0
while True:
    visited = [[0] * N for _ in range(N)]
    #연합 "들(복수형)" 을 넣을 배열 선언
    union_lst = []
    for y in range(N):
        for x in range(N):
            if visited[y][x] <= 0:
                BFS(y, x)

    #완탐이 끝난 이후, MyMap 값 업데이트. union_lst 내에는 각 하위 연합에 대한 배열이 존재함
    if union_lst:
        #하위 연합 배열에 대한 반복문
        for i in range(len(union_lst)):
            #하위 연합 길이
            MyLen = len(union_lst[i])
            #하위 연합의 총 합 계산
            MySum = 0
            for j in union_lst[i]:
                MySum += MyMap[j[0]][j[1]]
                visited[j[0]][j[1]] = 1

            #하위 연합별 평균값을 구한 후, MyMap내 값 업데이트
            avg = int(MySum // MyLen)
            for j in union_lst[i]:
                MyMap[j[0]][j[1]] = avg

    #반복문 종료 조건. visited 배열이 전부 -1 인 경우(더이상 연합 생성 불가) while문 종료
    if Check():
        break
    cnt += 1

print(cnt)

