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

def Check():
    global N
    for y in range(N):
        for x in range(N):
            if visited[y][x] == 0: return False
    return True

def IsSafe(y,x):
    return 0<=y<N and 0<=x<N


def BFS(init_y, init_x):
    global L, R, cnt

    visited[init_y][init_x] = 1
    Q.append([init_y, init_x])
    union_lst.append([init_y,init_x])
    flag = False

    while Q:
        y,x = Q.pop(0)
        for dir in range(4):
            n_y = y + dy[dir]
            n_x = x + dx[dir]
            if IsSafe(n_y, n_x) and L <= abs(MyMap[y][x] - MyMap[n_y][n_x]) <= R and not visited[n_y][n_x]:
                visited[n_y][n_x] = 1
                Q.append([n_y, n_x])
                union_lst.append([n_y, n_x])

            if IsSafe(n_y, n_x) and visited[n_y][n_x]:
                flag = True

    N = len(union_lst)
    MySum, avg = 0, 0
    if N == 1 and flag == False:
        visited[init_y][init_x] = 0
        return
    elif N > 1:
        cnt += 1
        for nation in union_lst:
            MySum += MyMap[nation[0]][nation[1]]
        avg = int(MySum // N)
        for nation in union_lst:
            MyMap[nation[0]][nation[1]] = avg


N, L, R = map(int, input().split())
MyMap = [list(map(int, input().split())) for _ in range(N)]

#상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


cnt = 0
while True:
    visited = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            union_lst = []
            Q = []
            BFS(y, x)
            union_lst = []
    # cnt += 1
    if Check(): break

print(cnt)